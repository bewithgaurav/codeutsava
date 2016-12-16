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

# Members
# +----+--------+----------------------------+----------+----------+--------+--------+----------+---------+
# | id | active | email                      | teamname | FullName | resume | github | graduate | contact |
# +----+--------+----------------------------+----------+----------+--------+--------+----------+---------+

app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.zoho.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'gauravtatti@zoho.com',
    MAIL_PASSWORD = 'Nezaflo69'
    )

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
    print(f,hashstring,"update members set active=%s where id=%s",('1',id))
    if f==hashstring:
        print("yes equal")
        try:
            cursor.execute("""update members set active=%s where id=%s""",('1',id))
            db.commit()
            return render_template("activated.html",value=True)
        except:
            db.rollback()
            return render_template("activated.html",value=False)
    return render_template("activated.html",value=False)


@app.route('/staffprofile',methods=['GET', 'POST'])
def staffprofile():
    if "staff" in session:
        fullname=session["staffname"]
        return render_template("staffprofile.html",name=fullname)
    return "Please Log In first"

@app.route('/staff',methods=['GET', 'POST'])
def staff():
    if "staff" in session:
        return redirect(url_for('staffprofile'))
    if request.method=='POST':
        uname=request.form.get('uname','')
        password=request.form.get('password','')
        query="select * from staff where username='%s' and password='%s'"%(uname,password)
        # print(query)
        cursor.execute(query)
        data=cursor.fetchone()
        # print(data)
        if (data):
            session["staff"]="yes"
            session["staffusername"]=uname
            session["staffpassword"]=password
            session["staffname"]=data[3]
            session["staffid"]=data[0]
            return redirect(url_for('staffprofile'))
        else:
            flash("Wrong Username/Password")
    return render_template("staff.html")

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
        return render_template("teamprofile.html",data=data,teamname=teamname)
        


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
                print(data)
                session['team']=uname
                return redirect(url_for('teamprofile'))
            else:
                flash("Invalid Credentials") 
    return render_template("login.html")

@app.route('/issuebooks',methods=['GET', 'POST'])
def issuebooks():
    session.permanent=True;
    if 'staff' in session: 
        if request.method=="POST":
            bid=request.form.get('bid','')
            stuname=request.form.get('stuname','')
            issuedate=request.form.get('issuedate','')
            staffid=session["staffid"]
            duedate=request.form.get('duedate','')
            if not bid or not stuname or not issuedate or not duedate:
                flash("Please enter all the Details")
            else:
                query="select * from issue where bookid='%s'"%bid
                cursor.execute(query)
                x=cursor.fetchone()
                if x:
                    flash("Book Currently Not Available")
                    return render_template("issuebooks.html")
                try:
                    query="select * from book where id='%d'"%int(bid)
                    cursor.execute(query)
                    y=cursor.fetchone()
                    if not y:
                        flash("Book Does Not Exist")
                        return render_template("issuebooks.html")
                except:
                    pass
                query="select id from student where username='%s'"%stuname
                cursor.execute(query)
                data=cursor.fetchone()
                # print("data",data)
                if not data:
                    flash("Wrong Username provided")
                else:
                    data=str(data[0])
                    try:
                        cursor.execute("""INSERT INTO issue (bookid, studentid, staffid, issuedate, duedate) VALUES (%s,%s,%s,%s,%s)""",(bid,data,staffid,issuedate,duedate))
                        print(bid,stuname,issuedate,duedate,staffid)
                        db.commit()
                        flash("Successfully Issued")
                    except:
                        db.rollback()
        return render_template("issuebooks.html")
    else:
        return "Please Log in First"


@app.route('/staffadd',methods=['GET', 'POST'])
def staffadd():
    if 'admin' in session:
        if request.method=='POST':
            uname=request.form.get('uname','')
            fullname=request.form.get('fullname','')
            password=request.form.get('password','')
            if not uname or not fullname or not password:
                flash("Please fill all the fields", "error")
            else:
                # query="INSERT INTO student (username, fullname, password) VALUES ('"+uname+"', '"+fullname+"', '"+password+"');"
                try:
                   cursor.execute("""INSERT INTO staff (username, password, fullname) VALUES (%s,%s,%s)""",(uname,password,fullname))
                   db.commit()
                except:
                   db.rollback()

                # print(query)
                # cursor.execute(query)
        query="select * from staff"
        cursor.execute(query)
        data=cursor.fetchall()
        return render_template("staffadd.html",data=data)
    else:
        return "Please Log in First"

@app.route('/searchstu',methods=['GET','POST'])
def searchstu():
    if 'student' in session:
        data=[]
        if request.method=="POST":
            username=session['studentusername']
            fullname=request.form.get('fullname','')
            query="select * from student where fullname='%s'"%(fullname)
            cursor.execute(query)
            data=cursor.fetchall()
            if not data:
                flash("No records Found")
        return render_template("searchstu.html",data=data)
    else:
        return "Please Log In First"

@app.route('/searchbooks',methods=['GET','POST'])
def searchbooks():
    if 'student' in session:
        data=[]
        if request.method=="POST":
            username=session['studentusername']
            booktitle=request.form.get('booktitle','')
            bookauthor=request.form.get('bookauthor','')
            if not bookauthor and not booktitle:
                flash("Enter Details")
            else:
                if booktitle and bookauthor:
                    query="select * from book where title='%s' and author='%s'"%(booktitle,bookauthor)
                elif booktitle:
                    query="select * from book where title='%s'"%(booktitle)
                else:
                    query="select * from book where author='%s'"%(bookauthor)
                cursor.execute(query)
                data=cursor.fetchall()    
                if not data:
                    flash("No records Found")
        return render_template("searchbooks.html",data=data)
    else:
        return "Please Log In First"

@app.route('/mybooks',methods=['GET','POST'])
def mybooks():
    if 'student' in session:
        username=session['studentusername']
        query="select id  from student where username='%s'"%(username)
        cursor.execute(query)
        data=cursor.fetchone()
        data=str(data[0])
        query="select *  from issue where studentid='%s'"%(data)
        cursor.execute(query)
        data=cursor.fetchall()
        newdata=[]
        if not data:
            flash("No Records Found")
        # print(query,data)
        else:
            newdata=[]
            for i in data:
                # x=[]
                bookid=i[0]
                query="select *  from book where id='%s'"%(bookid)
                cursor.execute(query)
                data2=cursor.fetchone()
                j=list(data2)+list(i[3:])
                newdata.append(j)
                # i.append(data2)
            print(newdata)
        return(render_template("mybooks.html",data=newdata)) 


if __name__ == '__main__':
    app.run( debug=True )