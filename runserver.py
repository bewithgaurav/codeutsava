from flask import *
import MySQLdb
import os
from datetime import *
from flask_mail import Mail, Message
import hashlib

db = MySQLdb.connect("localhost","root","toor","libmanage")
cursor = db.cursor()
app = Flask(__name__)
app.secret_key = os.urandom(24)

# +----+--------+-------+----------+--------+--------+---------+--------+------+------+------------+---------+-------+------+------+--------+--------+
# | id | active | email | teamname | resume | github | contact | gender | dob  | yop  | experience | address | state | city | name | degree | stream |
# +----+--------+-------+----------+--------+--------+---------+--------+------+------+------------+---------+-------+------+------+--------+--------+

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gauravandsanskar@gmail.com'
app.config['MAIL_PASSWORD'] = '8602229193'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/',methods=['GET', 'POST'])
def index():
    if 'team' in session:
        return redirect(url_for('teamprofile'))
    return render_template("index.html")

@app.route('/admin',methods=['GET', 'POST'])
def admin():
    if request.method=='POST':
        x=request.form.get('password','')
        if x=='toor':
            session['admin']='yes'
        else:
            return("Wrong Password. Please Try Again.")
            
        return render_template("admin.html")
    else:
        return "Please Log in First"

@app.route('/logout')
def logout():
    if 'deleted' in session:
        return render_template("login.html",teamname=session['team'])
    session.clear()
    return render_template("index.html")

@app.route('/student',methods=['GET', 'POST'])
def student():
    # print(session["student"])
    if "student" in session:
        return redirect(url_for('studentprofile'))
    if request.method=='POST':
        uname=request.form.get('uname','')
        password=request.form.get('password','')
        query="select * from student where username='%s' and password='%s'"%(uname,password)
        # print(query)
        cursor.execute(query)
        data=cursor.fetchone()
        # print(data)
        if (data):
            session["student"]="yes"
            session["studentusername"]=uname
            session["studentpassword"]=password
            session["studentname"]=data[3]
            session["studentid"]=data[0]
            return redirect(url_for('studentprofile'))
        else:
            flash("Wrong Username/Password")
    return render_template("student.html")

@app.route('/activate',methods=['GET', 'POST'])
def activate():
    email=request.args.get('email')
    hashstring=request.args.get('hash')
    query="select id from members where email='%s'"%(email)
    cursor.execute(query)
    id=cursor.fetchone()
    id=str(id[0])
    f=(hashlib.md5(id.encode('utf-8')).hexdigest())
    # print(f,hashstring,"update members set active=%s where id=%s",('1',id))
    if f==hashstring:
        # print("yes equal")
        try:
            cursor.execute("""update members set active=%s where id=%s""",('1',id))
            db.commit()
            return render_template("activated.html",value=True)
        except:
            db.rollback()
            return render_template("activated.html",value=False)
    return render_template("activated.html",value=False)

@app.route('/memberprofile',methods=['GET','POST'])
def memprofile():
    if 'team' not in session:
        return("You Need to Login first")
    if request.method=='POST':
        name=request.form.get('name','')
        gender=request.form.get('gender','')
        github=request.form.get('github','')
        resume=request.form.get('resume','')
        yop=request.form.get('yop','')
        contact=request.form.get('contact','')
        experience=request.form.get('experience','')
        address=request.form.get('address','')
        degree=request.form.get('degree','')
        stream=request.form.get('stream','')
        city=request.form.get('city','')
        state=request.form.get('state','')
        dob=request.form.get('dob','')
        # print("DATEOFBIRTH", dob)
        try:
            print(session['currentmember'])
            # print("UPDATE members set status=%d,name='%s',gender='%s',github='%s',resume='%s',yop='%s',contact='%s',experience='%s',address='%s',degree='%s',stream='%s',city='%s',state='%s',dob='%s'  where email='%s'"%(1,name,gender,github,resume,yop,contact,experience,address,degree,stream,city,state,dob,session["currentmember"]))
            cursor.execute("""UPDATE members set status=%s,name=%s,gender=%s,github=%s,resume=%s,yop=%s,contact=%s,experience=%s,address=%s,degree=%s,stream=%s,city=%s,state=%s,dob=%s where email=%s""",('1',name,gender,github,resume,yop,contact,experience,address,degree,stream,city,state,dob,session["currentmember"]))
            # cursor.execute("""update members set status=%s where email=%s""",('1',session["currentmember"]))
            db.commit()
            flash('Successfully Saved')
        except:
            db.rollback()
            flash('Error Occurred')
    if request.args.get('email'):
        session['currentmember']=request.args.get('email')
    query="select status from members where email='%s'"%(session['currentmember'])
    cursor.execute(query)
    data=cursor.fetchone()
    data=data[0]
    if data:
        decision='Edit'
        query="select * from members where email='%s'"%(session['currentmember'])
        cursor.execute(query)
        d=cursor.fetchone()
        d=list(d)
        for i in range(len(d)):
            if d[i]:
                continue
            else:
                d[i]=""
    else:
        decision='Add'
    return render_template("memberprofile.html",email=session['currentmember'],decision=decision,data=d)
@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method=="POST":
        uname=request.form.get('uname','')
        password=request.form.get('password','')
        email1=request.form.get('email1','')
        email2=request.form.get('email2','')
        email3=request.form.get('email3','')
        institute=request.form.get('institute','')
        if uname and password and email1 and email2 and email3 and institute:
            query="select * from teams where teamname='%s'"%(uname)
            cursor.execute(query)
            data=cursor.fetchone()
            if data:
                flash("Team Already Exists")
            else:
                try:
                    cursor.execute("""INSERT INTO teams (teamname, password) VALUES (%s,%s)""",(uname,password))
                    cursor.execute("""INSERT INTO members (teamname, email) VALUES (%s,%s)""",(uname,email1))
                    cursor.execute("""INSERT INTO members (teamname, email) VALUES (%s,%s)""",(uname,email2))
                    cursor.execute("""INSERT INTO members (teamname, email) VALUES (%s,%s)""",(uname,email3))
                    try:
                        query="select id from members where email='%s'"%(email1)
                        cursor.execute(query)
                        id1=cursor.fetchone()
                        id1=str(id1[0])
                        print("tatti",id1)
                        f=str(hashlib.md5(id1.encode('utf-8')).hexdigest())
                        print(f)
                        msgstring='Click here to confirm - '+'http://localhost:5000/activate?email='+email1+'&hash='+f 
                        print("Hello")
                        
                        msg = Message("registration successful", sender = 'gauravtatti@zoho.com', recipients = [email1])
                        msg.body = msgstring
                        mail.send(msg)
                        
                        query="select id from members where email='%s'"%(email2)
                        cursor.execute(query)
                        id2=cursor.fetchone()
                        id2=str(id2[0])
                        f=(hashlib.md5(id2.encode('utf-8')).hexdigest())
                        msgstring='Click here to confirm - '+'http://localhost:5000/activate?email='+email2+'&hash='+f 
                        msg = Message("registration successful", sender = 'gauravtatti@zoho.com', recipients = [email2])
                        msg.body = msgstring
                        mail.send(msg)
                        
                        query="select id from members where email='%s'"%(email3)
                        cursor.execute(query)
                        id3=cursor.fetchone()
                        id3=str(id3[0])
                        f=(hashlib.md5(id3.encode('utf-8')).hexdigest())
                        msgstring='Click here to confirm - '+'http://localhost:5000/activate?email='+email3+'&hash='+f 
                        msg = Message("registration successful", sender = 'gauravtatti@zoho.com', recipients = [email3])
                        msg.body = msgstring
                        mail.send(msg)
                        
                        flash("Emails sent, Please Verify E-mail IDs")
                        db.commit()
                    
                    except:
                        flash("There was a Problem sending Mails")
                except:
                   db.rollback()
                   flash("Unexpected Error occurred")
        else:
            flash("Enter All the fields")
    return render_template("register.html")

@app.route('/teamprofile',methods=['GET', 'POST'])
def teamprofile():
    if 'team' in session:
        teamname=session['team']
        query="select * from members where teamname='%s'"%(teamname)
        cursor.execute(query)
        data=cursor.fetchall()
        # print("tatti",dat)
        mem1=data[0]
        mem2=data[1]
        mem3=data[2]
        active1=mem1[1]
        active2=mem2[1]
        active3=mem3[1]
        return render_template("teamprofile.html",data=data,teamname=teamname)
    return ("You need to Login First")
@app.route('/deleteteam',methods=['GET', 'POST'])
def deleteteam():
    if 'team' in session:
        teamname=session['team']
        try:
            cursor.execute("""delete from members where teamname='%s'""",(teamname))
            db.commit()
            session['deleted']=1
            return redirect(url_for(logout))
        except:
            db.rollback()
            flash("A problem occurred during deletion. Please try again")
        return render_template("teamprofile.html")
        

@app.route('/login',methods=['GET', 'POST'])
def login():
    if 'team' in session:
        return redirect(url_for('teamprofile'))
    if request.method=='POST':
        uname=request.form.get('uname','')
        password=request.form.get('password','')
        if uname and password:
            query="select * from teams where teamname='%s' and password='%s'"%(uname,password)
            cursor.execute(query)
            data=cursor.fetchone()
            if data:
                session['team']=uname
                return redirect(url_for('teamprofile'))
            else:
                flash("Invalid Credentials") 
    return render_template("login.html")


if __name__ == '__main__':
    app.run( debug=True )