from flask import *
import MySQLdb
import os
from datetime import *
from flask_mail import Mail, Message
import hashlib
from datetime import datetime
import string
import random
from flask_recaptcha import ReCaptcha
try:
	# For Python 3.0 and later
	from urllib.request import urlopen
except ImportError:
	# Fall back to Python 2's urllib2
	from urllib2 import urlopen
# try:
#     import sys
#     reload(sys)
#     sys.setdefaultencoding("utf-8")
# except:
#     pass

db = MySQLdb.connect("localhost","root","toor","codeutsava")
db.ping(True)
cursor = db.cursor()
app = Flask(__name__)
# app.secret_key = os.urandom(24)
app.secret_key = 'lAltCodeUtsvaGaurAvMayaNk'
# +----+--------+-------+----------+--------+--------+---------+--------+------+------+------------+---------+-------+------+------+--------+--------+
# | id | active | email | teamname | resume | github | contact | gender | dob  | yop  | experience | address | state | city | name | degree | stream |
# +----+--------+-------+----------+--------+--------+---------+--------+------+------+------------+---------+-------+------+------+--------+--------+
# recaptcha = ReCaptcha()
# recaptcha.init_app(app)
# recaptcha = ReCaptcha(app=app)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'Codeutsava@codeutsava.in'
# app.config['MAIL_PASSWORD'] = '8602229193'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SERVER']='smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = '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'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG']= True
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'apikey'
# app.config['MAIL_PASSWORD'] = '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'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_DEBUG']= True
mail = Mail(app)
# recaptcha = ReCaptcha(site_key="6LcbfhEUAAAAALPhMJ07H7AHvqn6X4M4DBRIoVNr", secret_key="6LcbfhEUAAAAACgg5XiNL3wNLwAmi5wmYhGM7Sv_")    
# RECAPTCHA_ENABLED = True
# RECAPTCHA_SITE_KEY = "6LcbfhEUAAAAALPhMJ07H7AHvqn6X4M4DBRIoVNr"
# RECAPTCHA_SECRET_KEY = "6LcbfhEUAAAAACgg5XiNL3wNLwAmi5wmYhGM7Sv_"
# RECAPTCHA_THEME = "dark"
# RECAPTCHA_TYPE = "image"
# RECAPTCHA_SIZE = "compact"
# RECAPTCHA_TABINDEX = 10
# print(recaptcha.get_code())
SITE_KEY = "6LcbfhEUAAAAALPhMJ07H7AHvqn6X4M4DBRIoVNr"
SECRET_KEY = "6LcbfhEUAAAAACgg5XiNL3wNLwAmi5wmYhGM7Sv_"


def checkRecaptcha(response, secretkey):
	url = 'https://www.google.com/recaptcha/api/siteverify?'
	url = url + 'secret=' +secretkey
	url = url + '&response=' +response
	try:
		jsonobj = json.loads(urlopen(url).read())
		if jsonobj['success']:
			return True
		else:
			return False
	except Exception as e:
		print(str(e))
	return False

def some_random_string(size=8, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

@app.before_request
def csrf_protect():
	if request.method == "POST":
		token = session.pop('_csrf_token', None)
		if not token or token != request.form.get('_csrf_token'):
			abort(403)

def generate_csrf_token():
	if '_csrf_token' not in session:
		session['_csrf_token'] = some_random_string()
		# print(session['_csrf_token'])
	return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token


@app.route('/')
def home():
	return render_template("index.html")
@app.route('/techTalk')
def techTalk():
    return render_template("techtalks.html")
@app.route('/blogs',methods=['GET'])
def blogs():
	blog=str(request.args.get('page'))
	try:
		blogInt=int(blog)
	except Exception as e:
		return render_template("blog.html")
	if blogInt>=1 and blogInt<=8:
		return render_template("blog"+blog+".html")       
	else:
		return render_template("blog.html")



@app.route('/registration',methods=['GET', 'POST'])
def index():
	if 'team' in session:
		return redirect(url_for('teamprofile'))
	return render_template("registerindex.html")

@app.route('/workshopregister',methods=['GET', 'POST'])
def workshopregister():
	if 'team' in session:
		return redirect(url_for('teamprofile'))
	return render_template("workshopindex.html")

@app.route('/logout')
def logout():
	if 'deleted' in session:
		teamname=session['team']
		session.clear()
		return render_template("login.html",teamname=teamname)
	session.clear()
	return redirect(url_for('index'))
@app.route('/hackathon',methods=['GET', 'POST'])
def hackathon():
	return render_template("hackathon.html")
	

@app.route('/activate',methods=['GET', 'POST'])
def activate():
	email=request.args.get('email')
	hashstring=request.args.get('hash')
	
	#Matching the hash received with the one from database
	query="select id from members where email=%s"
	cursor.execute(query,[email])
	id=cursor.fetchone()
	# id=str(id[0])
	reverse=str(id[0])+email
	f=(hashlib.md5(reverse.encode('utf-8')).hexdigest())
	print(f,hashstring,reverse)
	if f!=hashstring:
		return "INVALID URL"
	# If email ALready Exists
	query="select teamname from members where email=%s and active=%s"
	cursor.execute(query,[email,'1'])
	d=cursor.fetchone()
	if d:
		query="select password from teams where teamname=%s"
		cursor.execute(query,[d[0]])
		password=cursor.fetchone()
		password=password[0]
		return render_template("activated.html",exist=1,teamname=d[0],password=password)
	
	#For displaying Teamname and Password
	try:
		query="select teamname from members where email=%s"
		cursor.execute(query,[email])
		d=cursor.fetchone()
		teamname=d[0]
		query="select password from teams where teamname=%s"
		cursor.execute(query,[teamname])
		d=cursor.fetchone()
		password=d[0]
	except:
		pass
	#Matching the hash received with the one from database
	query="select id from members where email=%s"
	cursor.execute(query,[email])
	id=cursor.fetchone()
	# id=str(id[0])
	reverse=str(id[0])+email
	f=(hashlib.md5(reverse.encode('utf-8')).hexdigest())
	print(f,hashstring,reverse)
	if f==hashstring:
		print("yes equal")
		try:
			cursor.execute("""update members set active=%s where id=%s""",['1',id])
			db.commit()
			return render_template("activated.html",value=True,teamname=teamname,password=password)
		except:
			db.rollback()
			return render_template("activated.html",value=False)
	return render_template("activated.html",value=False)

@app.route('/allteams')
def showall():
	# print("heywassup")
	q="select teamname,institute,active from teams"
	cursor.execute(q)
	d=cursor.fetchall()
	l=[]
	for i in d:
		l.append((i[0],i[1],i[2]))
	return render_template('allteams.html',data=l)  

@app.route('/viewteam',methods=['GET','POST'])
def viewteam():
	name=str(request.args.get('team'))
	q="select name,degree,stream from members where teamname=%s"
	cursor.execute(q,[name])
	d=cursor.fetchall()
	# print(d)
	q="select active,institute from teams where teamname=%s"
	cursor.execute(q,[name])
	teamstatus=cursor.fetchone()
	institute=teamstatus[1]
	teamstatus=teamstatus[0]
	if d:
		c=[]
		for i in d:
			c.append((i[0],i[1],i[2]))
		print(c)
	else:
		return("Wrong Team Name")
	return render_template('viewteam.html',data=c,teamname=name,teamstatus=teamstatus,institute=institute)

@app.route('/resend',methods=['GET'])
def resend():
	if 'team' not in session:
		return("You Need to Login first")
	resendemail=request.args.get('email')
	try:
		query="select id from members where email=%s"
		cursor.execute(query,[resendemail])
		id1=cursor.fetchone()
		id1=str(id1[0])+resendemail
		f=str(hashlib.md5(id1.encode('utf-8')).hexdigest())
		# msgstring='Click here to confirm the registration for your team '+session['team']+'- '+'http://codeutsava.in/activate?email='+resendemail+'&hash='+f 
		msg = Message("Team Registration Successful", sender = 'Codeutsava@codeutsava.in', recipients = [resendemail])
		# msg.body = msgstring
		msg.html = render_template('email.html', teamname=session['team'],email=resendemail, hash=f)
						
		mail.send(msg)
		flash("Confirmation Mail sent to "+resendemail+". Please check Spam Folder.")
	except Exception as e:
		print(str(e))
		flash("An Error Occurred")
	return redirect(url_for("teamprofile"))

@app.route('/linuxregister',methods=['GET','POST'])
def linuxregister():
	success=False
	if request.method=='POST':
		response = request.form.get('g-recaptcha-response')
		if checkRecaptcha(response,SECRET_KEY):
			name=request.form.get('name','')
			email=request.form.get('email','')
			yop=request.form.get('yop','')
			institute=request.form.get('institute','')
			contact=request.form.get('contact','')
			experience=request.form.get('experience','')
			degree=request.form.get('degree','')
			stream=request.form.get('stream','')
			print(name,email,yop,institute,contact,experience,degree,stream)
			try:
				cursor.execute("""INSERT INTO linuxworkshop (name,email,yop,institute,contact,experience,degree,stream) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",[name,email,yop,institute,contact,experience,degree,stream])
				db.commit()
				success=True
			except Exception as e:
				db.rollback()
				print(str(e))
				flash("An Error Occurred. Please Try Later")
		else:
			flash("Captcha Could not be Verified")
	return render_template("linuxregister.html",success=success)


@app.route('/pythonregister',methods=['GET','POST'])
def pythonregister():
	success=False
	if request.method=='POST':
		response = request.form.get('g-recaptcha-response')
		if checkRecaptcha(response,SECRET_KEY):
			print("yeah")
			name=request.form.get('name','')
			email=request.form.get('email','')
			yop=request.form.get('yop','')
			contact=request.form.get('contact','')
			degree=request.form.get('degree','')
			stream=request.form.get('stream','')
			try:
				cursor.execute("""INSERT INTO pythonworkshop (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
				db.commit()
				success=True
			except:
				db.rollback()
				print(str(e))
				flash("An Error Occurred. Please Try Later")
		else:
			flash("Captcha Could not be Verified")
		
	return render_template("pythonregister.html",success=success)
@app.route('/workshop1register',methods=['GET','POST'])
def workshop1register():
    success=False
    if request.method=='POST':
        response = request.form.get('g-recaptcha-response')
        if checkRecaptcha(response,SECRET_KEY):
            print("yeah")
            name=request.form.get('name','')
            email=request.form.get('email','')
            yop=request.form.get('yop','')
            contact=request.form.get('contact','')
            degree=request.form.get('degree','')
            stream=request.form.get('stream','')
            try:
                cursor.execute("""INSERT INTO workshop1 (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
                db.commit()
                success=True
            except:
                db.rollback()
                print(str(e))
                flash("An Error Occurred. Please Try Later")
        else:
            flash("Captcha Could not be Verified")
        
    return render_template("workshop1.html",success=success)    
@app.route('/workshop2register',methods=['GET','POST'])
def workshop2register():
    success=False
    if request.method=='POST':
        response = request.form.get('g-recaptcha-response')
        if checkRecaptcha(response,SECRET_KEY):
            print("yeah")
            name=request.form.get('name','')
            email=request.form.get('email','')
            yop=request.form.get('yop','')
            contact=request.form.get('contact','')
            degree=request.form.get('degree','')
            stream=request.form.get('stream','')
            try:
                cursor.execute("""INSERT INTO workshop2 (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
                db.commit()
                success=True
            except:
                db.rollback()
                print(str(e))
                flash("An Error Occurred. Please Try Later")
        else:
            flash("Captcha Could not be Verified")
        
    return render_template("workshop2.html",success=success)
@app.route('/workshop3register',methods=['GET','POST'])
def workshop3register():
    success=False
    if request.method=='POST':
        response = request.form.get('g-recaptcha-response')
        if checkRecaptcha(response,SECRET_KEY):
            print("yeah")
            name=request.form.get('name','')
            email=request.form.get('email','')
            yop=request.form.get('yop','')
            contact=request.form.get('contact','')
            degree=request.form.get('degree','')
            stream=request.form.get('stream','')
            try:
                cursor.execute("""INSERT INTO workshop3 (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
                db.commit()
                success=True
            except:
                db.rollback()
                print(str(e))
                flash("An Error Occurred. Please Try Later")
        else:
            flash("Captcha Could not be Verified")
        
    return render_template("workshop3.html",success=success)            
@app.route('/workshop4register',methods=['GET','POST'])
def workshop4register():
    success=False
    if request.method=='POST':
        response = request.form.get('g-recaptcha-response')
        if checkRecaptcha(response,SECRET_KEY):
            print("yeah")
            name=request.form.get('name','')
            email=request.form.get('email','')
            yop=request.form.get('yop','')
            contact=request.form.get('contact','')
            degree=request.form.get('degree','')
            stream=request.form.get('stream','')
            try:
                cursor.execute("""INSERT INTO workshop4 (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
                db.commit()
                success=True
            except:
                db.rollback()
                print(str(e))
                flash("An Error Occurred. Please Try Later")
        else:
            flash("Captcha Could not be Verified")
        
    return render_template("workshop4.html",success=success)
@app.route('/workshop5register',methods=['GET','POST'])
def workshop5register():
    success=False
    if request.method=='POST':
        response = request.form.get('g-recaptcha-response')
        if checkRecaptcha(response,SECRET_KEY):
            print("yeah")
            name=request.form.get('name','')
            email=request.form.get('email','')
            yop=request.form.get('yop','')
            contact=request.form.get('contact','')
            degree=request.form.get('degree','')
            stream=request.form.get('stream','')
            try:
                cursor.execute("""INSERT INTO workshop5 (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
                db.commit()
                success=True
            except:
                db.rollback()
                print(str(e))
                flash("An Error Occurred. Please Try Later")
        else:
            flash("Captcha Could not be Verified")
        
    return render_template("workshop5.html",success=success)
@app.route('/workshop6register',methods=['GET','POST'])
def workshop6register():
    success=False
    if request.method=='POST':
        response = request.form.get('g-recaptcha-response')
        if checkRecaptcha(response,SECRET_KEY):
            print("yeah")
            name=request.form.get('name','')
            email=request.form.get('email','')
            yop=request.form.get('yop','')
            contact=request.form.get('contact','')
            degree=request.form.get('degree','')
            stream=request.form.get('stream','')
            try:
                cursor.execute("""INSERT INTO workshop6 (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
                db.commit()
                success=True
            except:
                db.rollback()
                print(str(e))
                flash("An Error Occurred. Please Try Later")
        else:
            flash("Captcha Could not be Verified")
        
    return render_template("workshop6.html",success=success)
@app.route('/workshop7register',methods=['GET','POST'])
def workshop7register():
    success=False
    if request.method=='POST':
        response = request.form.get('g-recaptcha-response')
        if checkRecaptcha(response,SECRET_KEY):
            print("yeah")
            name=request.form.get('name','')
            email=request.form.get('email','')
            yop=request.form.get('yop','')
            contact=request.form.get('contact','')
            degree=request.form.get('degree','')
            stream=request.form.get('stream','')
            try:
                cursor.execute("""INSERT INTO workshop7 (name,email,yop,contact,degree,stream) VALUES (%s,%s,%s,%s,%s,%s)""",[name,email,yop,contact,degree,stream])
                db.commit()
                success=True
            except:
                db.rollback()
                print(str(e))
                flash("An Error Occurred. Please Try Later")
        else:
            flash("Captcha Could not be Verified")
        
    return render_template("workshop7.html",success=success)           

		
@app.route('/memberprofile',methods=['GET','POST'])
def memprofile():
	if 'team' not in session:
		return("You Need to Login first")
	if 'currentmember' not in session and not request.args.get('email'):
		return redirect(url_for("teamprofile"))
	if request.method=='POST':
		response = request.form.get('g-recaptcha-response')
		if checkRecaptcha(response,SECRET_KEY):
			name=request.form.get('name','')
			gender=request.form.get('gender','')
			github=request.form.get('github','')
			twitter=request.form.get('twitter','')
			resume=request.form.get('resume','')
			yop=request.form.get('yop','')
			contact=request.form.get('contact','')
			experience=request.form.get('experience','')
			address=request.form.get('address','')
			degree=request.form.get('degree','')
			stream=request.form.get('stream','')
			city=request.form.get('city','')
			tshirt=request.form.get('tshirt','')
			state=request.form.get('state','')
			dob=str(request.form.get('dob',''))
			try:
				# print(dob)
				dob =str(datetime.strptime(dob, '%d %B, %Y'))
				dob=dob.split()
				dob=dob[0]
				# print(dob)
			except:
				pass
			# print("DATEOFBIRTH", dob)
			# print("DATEOFBIRTH", str(datetime_object))
			try:
				# print(name,gender,github,resume,yop,contact,experience,address,degree,stream,city,state,dob,session["currentmember"])
				try:
					cursor.execute("""UPDATE list set name=%s,gender=%s,github=%s,resume=%s,yop=%s,contact=%s,experience=%s,address=%s,degree=%s,stream=%s,city=%s,state=%s,dob=%s,twitter=%s where email=%s""",[name,gender,github,resume,yop,contact,experience,address,degree,stream,city,state,dob,twitter,session["currentmember"]])
					# cursor.execute("""update members set status=%s where email=%s""",('1',session["currentmember"]))
					db.commit()
				except:
					pass
				# print("UPDATE members set status=%d,name='%s',gender='%s',github='%s',resume='%s',yop='%s',contact='%s',experience='%s',address='%s',degree='%s',stream='%s',city='%s',state='%s',dob='%s'  where email='%s'"%(1,name,gender,github,resume,yop,contact,experience,address,degree,stream,city,state,dob,session["currentmember"]))
				cursor.execute("""UPDATE members set tshirt=%s,status=%s,name=%s,gender=%s,github=%s,resume=%s,yop=%s,contact=%s,experience=%s,address=%s,degree=%s,stream=%s,city=%s,state=%s,dob=%s,twitter=%s where email=%s""",[tshirt,'1',name,gender,github,resume,yop,contact,experience,address,degree,stream,city,state,dob,twitter,session["currentmember"]])
				# cursor.execute("""update members set status=%s where email=%s""",('1',session["currentmember"]))
				db.commit()
				flash('Successfully Saved')
			except Exception as e:
				print(str(e))
				db.rollback()
				flash('Error Occurred while Updating the Database. Please Try Again ')

		else:
			flash("Captcha Could not be Verified")

	if request.args.get('email'):
		session['currentmember']=request.args.get('email')
	query="select status,active from members where email=%s"
	cursor.execute(query,[session['currentmember']])
	data=cursor.fetchone()
	data1=data[0]
	active=data[1]
	data=data1
	if not active:
		flash("Please verify %s to add Details. Check confirmation mail. If not present, Check Spam folder"%session['currentmember'])
		return redirect(url_for("teamprofile"))
	if data:
		decision='Edit/View'
		query="select * from members where email=%s"
		cursor.execute(query,[session['currentmember']])
		d=cursor.fetchone()
	else:
		decision="Add"
		d=[]
		for i in range(18):
			d.append('')
	return render_template("memberprofile.html",email=session['currentmember'],decision=decision,data=d)

@app.route('/register',methods=['GET', 'POST'])
def register():
	if 'team' in session:
		return redirect(url_for('teamprofile'))
	if request.method=="POST":
		response = request.form.get('g-recaptcha-response')
		if checkRecaptcha(response,SECRET_KEY):
			uname=request.form.get('uname','')
			password=request.form.get('password','')
			email1=request.form.get('email1','')
			email2=request.form.get('email2','')
			email3=request.form.get('email3','')
			institute=request.form.get('institute','')
			print(request.form.get('_csrf_token',''))
			if uname and password and email1 and email2 and email3 and institute:
				query="select * from members where email=%s"
				cursor.execute(query,[email1])
				data1=cursor.fetchone()
				query="select * from members where email=%s"
				cursor.execute(query,[email2])
				data2=cursor.fetchone()
				query="select * from members where email=%s"
				cursor.execute(query,[email3])
				data3=cursor.fetchone()
				if data1 or data2 or data3:
					if data1:
						flash("Email ID "+email1+" already exists in team "+data1[3])
					if data2:
						flash("Email ID "+email2+" already exists in team "+data2[3])
					if data3:
						flash("Email ID "+email3+" already exists in team "+data3[3])
					return render_template("register.html")
				query="select * from teams where teamname=%s"
				cursor.execute(query,[uname])
				data=cursor.fetchone()
				if data:
					flash("Team Already Exists")
				else:
					try:
						cursor.execute("""INSERT INTO list (email) VALUES (%s)""",[email1])
					except:
						pass
					try:
						cursor.execute("""INSERT INTO list (email) VALUES (%s)""",[email2])
					except:
						pass
					try:
						cursor.execute("""INSERT INTO list (email) VALUES (%s)""",[email3])
					except:
						pass
					
					try:
						cursor.execute("""INSERT INTO teams (teamname, password, institute) VALUES (%s,%s,%s)""",[uname,password,institute])
						cursor.execute("""INSERT INTO members (teamname, email) VALUES (%s,%s)""",[uname,email1])
						cursor.execute("""INSERT INTO members (teamname, email) VALUES (%s,%s)""",[uname,email2])
						cursor.execute("""INSERT INTO members (teamname, email) VALUES (%s,%s)""",[uname,email3])
						try:
							query="select id from members where email=%s"
							cursor.execute(query,[email1])
							id1=cursor.fetchone()
							id1=str(id1[0])+email1
							# print("tatti",id1)
							f=str(hashlib.md5(id1.encode('utf-8')).hexdigest())
							print("hash id "+f)
							# msgstring='Click here to confirm the registration for your team '+uname+'- '+'http://codeutsava.in/activate?email='+email1+'&hash='+f 
							# print("Hello")
							
							msg = Message("Team Registration Successful", sender = 'Codeutsava@codeutsava.in', recipients = [email1])
							msg.html = render_template('email.html', teamname=uname,email=email1, hash=f)
							mail.send(msg)
							
							query="select id from members where email=%s"
							cursor.execute(query,[email2])
							id2=cursor.fetchone()
							id2=str(id2[0])+email2
							f=(hashlib.md5(id2.encode('utf-8')).hexdigest())
							print(f)
							# msgstring='Click here to confirm the registration for your team '+uname+'- '+'http://codeutsava.in/activate?email='+email2+'&hash='+f 
							msg = Message("Team Registration Successful", sender = 'Codeutsava@codeutsava.in', recipients = [email2])
							msg.html = render_template('email.html', teamname=uname,email=email2, hash=f)
							mail.send(msg)
							
							query="select id from members where email=%s"
							cursor.execute(query,[email3])
							id3=cursor.fetchone()
							id3=str(id3[0])+email3
							f=(hashlib.md5(id3.encode('utf-8')).hexdigest())
							print(f)
							# msgstring='Click here to confirm the registration for your team '+uname+'- '+'http://codeutsava.in/activate?email='+email3+'&hash='+f 
							msg = Message("Team Registration Successful", sender = 'Codeutsava@codeutsava.in', recipients = [email3])
							# msg.body = msgstring
							msg.html = render_template('email.html', teamname=uname,email=email3, hash=f)
							mail.send(msg)
		
							flash("Emails sent, Please Verify E-mail IDs. Be Sure to check the Spam Folder")
							db.commit()
						
						except:
							flash("There was a Problem sending Mails")
					except Exception as e:
					   print(str(e)) 
					   db.rollback()
					   flash("Unexpected Error occurred")
			else:
				flash("Enter All the fields")
		else:
			flash("Captcha Could not be Verified")
		
	return render_template("register.html")

@app.route('/viewmember', methods=['GET'])
def viewmember():
	if 'admin' in session:
		email=str(request.args.get('email'))
		query="select * from members where email=%s"
		cursor.execute(query,[email])
		member=cursor.fetchone()
		query="select teamname from members where email=%s"
		cursor.execute(query,[email])
		teamname=cursor.fetchone()
		teamname=teamname[0]
		query="select institute from teams where teamname=%s"
		cursor.execute(query,[teamname])
		institute=cursor.fetchone()
		institute=institute[0]
		return render_template("viewmember.html",i=member,institute=institute)
	else:
		return ("Stay where you belong. Please.")

@app.route('/adminpanel', methods=['GET', 'POST'])
def adminpanel():
	if 'team' in session:
		return("Denied")
	if request.method=="POST" or ('admin' in session):
		password=request.form.get('password','')
		ticket=hashlib.md5(password.encode('utf-8')).hexdigest()
		if ticket=="cd48af533cef6cb12a60c400dee83f76" or ('admin' in session):
			session["admin"]=1
			query="select * from members"
			cursor.execute(query)
			members=cursor.fetchall()
			query="select * from linuxworkshop"
			cursor.execute(query)
			linux=cursor.fetchall()
			query="select * from pythonworkshop"
			cursor.execute(query)
			python=cursor.fetchall()
			python=list(python)
			# print(python)
			for i in range(len(python)):
				python[i]=list(python[i])
				# print(python[i])
				for j in range(len(python[i])):
					try:
						python[i][j].encode('utf-8')
					except:
						pass
			linux=list(linux)
			for i in range(len(linux)):
				linux[i]=list(linux[i])
				for j in range(len(linux[i])):
					try:
						linux[i][j].encode('utf-8')
					except:
						pass
			members=list(members)
			for i in range(len(members)):
				members[i]=list(members[i])
				for j in range(len(members[i])):
					try:
						members[i][j].encode('utf-8')
					except:
						pass
			return render_template("adminpanel.html",members=members,linux=linux,python=python,memlen=len(members),linuxlen=len(linux),pythonlen=len(python))
		else:
			return ("Stay where you belong. Please.")
	return render_template("adminpassword.html")


@app.route('/teamprofile',methods=['GET', 'POST'])
def teamprofile():
	if 'team' in session:
		status="Incomplete"
		teamname=str(session['team'])
		query="select * from members where teamname=%s"
		cursor.execute(query,[teamname])
		data=cursor.fetchall()
		# print("tatti",dat)
		mem1=data[0]
		mem2=data[1]
		mem3=data[2]
		active1=mem1[1]
		active2=mem2[1]
		active3=mem3[1]
		query="select * from teams where teamname=%s"
		cursor.execute(query,[teamname])
		d=cursor.fetchone()
		institute=d[4]
		d=d[2]
		if d:
			status="Pending for Judgement"
		else:
			s1=mem1[17]
			s2=mem2[17]
			s3=mem3[17]
			if s1==1 and s2==1 and s3==1:
				try:
					cursor.execute("""update teams set active=%s where teamname=%s""",['1',teamname])
					status="Pending for Judgement"
					db.commit()
				except:
					db.rollback()
					flash('Error Occurred')

		return render_template("teamprofile.html",data=data,teamname=teamname,status=status,institute=institute)
	return render_template("thanks.html",msg="You need to Login First")


@app.route('/deleteteam',methods=['GET', 'POST'])
def deleteteam():
	if 'team' in session:
		teamname=session['team']
		try:
			query="select * from members where teamname=%s"
			cursor.execute(query,[teamname])
			data=cursor.fetchall()
			print(data)
			cursor.execute("delete from members where teamname=%s",[teamname])
			cursor.execute("delete from teams where teamname=%s",[teamname])
			db.commit()
			session['deleted']=1
			# print("tatti",dat)
			mem1=data[0]
			mem2=data[1]
			mem3=data[2]
			email1=mem1[2]
			email2=mem2[2]
			email3=mem3[2]
			try:
				# msgstring="Your team %s has been deleted"%(session['team'])
				msg = Message("Deletion of the team", sender = 'Codeutsava@codeutsava.in', recipients = [email1,email2,email3])
				# msg.body = msgstring
				msg.html = render_template('deleteemail.html', teamname=session['team'],email1=email1, email2=email2,email3=email3)
				mail.send(msg)
				print("DELETED")
				# return redirect(url_for('logout'))
			except:
				flash("Unable to send mail for deletion.")
			return redirect(url_for('logout'))
		except:
			db.rollback()
			flash("A problem occurred during deletion. Please try again")
		return render_template("teamprofile.html")
	else:
		return("You need to Login First")
		


@app.route('/login',methods=['GET', 'POST'])
def login():
	if 'team' in session:
		return redirect(url_for('teamprofile'))
	if request.method=='POST':
		response = request.form.get('g-recaptcha-response')
		if checkRecaptcha(response,SECRET_KEY):
			uname=request.form.get('uname','')
			password=request.form.get('password','')
			if uname and password:
				query="select * from teams where teamname=%s and password=%s"
				cursor.execute(query,[uname,password])
				data=cursor.fetchone()
				if data:
					session['team']=uname
					return redirect(url_for('teamprofile'))
				else:
					flash("Invalid Credentials") 
		else:
			flash("Captcha Could not be Verified")
		
	return render_template("login.html")

# Jim Moriarty. Hi. Thanks for Checking out the code.

if __name__ == '__main__':
	app.run( debug=True )
