from flask import Flask,redirect,render_template,request,url_for,session,make_response
import requests
from datetime import date
import smtplib
from email.mime.text import MIMEText
from flask_sqlalchemy import SQLAlchemy
import shelve
import os
import time
os.environ["TZ"] = "Asia/Calcutta"
time.tzset()
format = "%Y-%m-%d %H:%M:%S"
import calendar
from pytz import timezone
from tzlocal import get_localzone
Fetch_url='https://newsapi.org/v2/everything?'
api_key='Your api key'

'''
now_utc = datetime.now(timezone('UTC'))
    now_local = now_utc.astimezone(get_localzone())
    li=now_local.strftime(format)
    li=li.split(' ')
    cal=li[0].split('-')
    time=li[1]
    mon=calendar.month_name[int(cal[1])]
    year=cal[0]
    date=cal[2]
    '''

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = "sujith"

'''app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SQLALCHEMY_DATABASE_URI']='oracle://mk:123@localhost:1521/XE'''

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="username", 
    password="password",
    hostname="hostname.mysql.pythonanywhere-services.com",
    databasename="databasename",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class user97(db.Model):
    __tablename__ = 'Quickes_users'
    id =db.Column(db.Integer,db.Sequence('seq_book',start=1),primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(40))
    Password = db.Column(db.String(40))

def send_email(reciveremail,name):
    try:
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'contactquickes@gmail.com' #mail id
        password = 'yourpassword' #yourpassword
        sender = 'contactquickes@gmail.com'
        targets = reciveremail
        msg = MIMEText('Hello  {} !,Welcome to Quickes ! Stay updated anywhere.Here after you will receive our site updates of our site.        Stay safe and stay updated.   \n \n\n                          Thank You  \n\n \n                                                 - visit again : {}'.format(name,'http://quickes.pythonanywhere.com/'))
        msg['Subject'] = 'Quickes-Reg'
        msg['From'] = sender
        msg['To'] = targets

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username,password)
        server.sendmail(sender,targets,msg.as_string())
        server.quit()
    except:
        pass

@app.route('/Home')
@app.route('/')
def index():
    try:
        session["user_data"]=request.cookies.get("User_id")

        if  session["user_data"] != None:
            resp = make_response(render_template('home.html',log_link="/profile",log = session["user_data"],btn_color="btn-success",fs="12px"))
            return resp
        else:
            return render_template('home.html',log="login",log_link="/login",btn_color="btn-danger",fs="auto")

    except:
        return render_template('home.html',log="login",log_link="/login",btn_color="btn-danger",fs="auto")


@app.route('/profile')
def profile():
    d= user97.query.filter_by(email=request.cookies.get("User_id")).first()
    return render_template('profile.html',name=d.username,mail=d.email,password=d.Password)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session["usr_id"] = request.form['email']
        session["Password"] = request.form['psw']
        try:
            d= user97.query.filter_by(email=session['usr_id']).first()
            if d.email == session["usr_id"] or d.email == session["usr_id"].lower():
                if d.Password == session["Password"]:
                    res= make_response(redirect(url_for('index')))
                    res.set_cookie("User_id",session['usr_id'],60*60*24*365*5)
                    return res
                else:
                    return render_template('login.html',noacc="passsword incorrrect")
            else:
                return render_template('login.html',noacc="User id incorrrect")
        except:
            return render_template('login.html',noacc="User id or passsword incorrrect")



    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    res= make_response(redirect(url_for('index')))
    res.delete_cookie("User_id")
    return res


@app.route('/reg',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        session['usr_name'] = request.form['usr_name']
        session['usr_id'] = request.form['email'].lower()
        session['Password'] = request.form['psw']
        session['psw_repeat'] = request.form['psw-repeat']
        if session['Password'] == session['psw_repeat']:
            try:
                d=user97.query.filter_by(email=session['usr_id']).first()
                if  d.email != None:
                    return render_template('reg.html',user_alart="User Found")
            except:
                res= make_response(redirect(url_for('index')))
                res.set_cookie("User_id",session['usr_id'].lower(),60*60*24*365*5)

                try:
                    register = user97(username = session['usr_name'], email = session['usr_id'],Password = session['Password'])
                    db.session.add(register)
                    db.session.commit()
                    send_email(session['usr_id'],session['usr_name'])
                except:
                    pass
                return res

        else:
            return render_template('reg.html',user_alart="Password miss match")
    else:
        return render_template('reg.html')

@app.route('/trending')
def home():
    title,photo,url=[],[],[]
    def get_articles(file):
        for i in range(len(file)):
            title.append(file[i]['title'])
            photo.append(file[i]['urlToImage'])
            url.append(file[i]['url'])

    f_url='https://newsapi.org/v2/everything?'

    api_key='api key'

    perameters={
        'q':'news',
        'pagesize':100,
        'apiKey' : api_key,
        'language' : 'en',
        'from' : date.today()
    }

    response=requests.get(f_url,params=perameters)
    response_json= response.json()
    get_articles(response_json['articles'])

    def bind(url,photo,title):
            binded_list=[]
            for i in range(0,len(url),3):
                try:
                    t,ls=0,[]
                    k = i
                    while t < 3:
                        ls.append(url[k+t])
                        ls.append(photo[k+t])
                        ls.append(title[k+t])
                        t+=1
                    binded_list.append(ls)
                except:
                    return binded_list

    bils=bind(url,photo,title)
    """for i in range(len(bils)):
        if bils[i][2] != None:
            bils[i][2] = transulator.translate(bils[i][2],dest='hi').text
        if bils[i][5] != None:
            bils[i][5] = transulator.translate(bils[i][5],dest='hi').text
        if bils[i][8] != None:
            bils[i][8] = transulator.translate(bils[i][8],dest='hi').text
        """

    try:
        if bils != []:
            return render_template('trending.html',ls=bils)
        else:
            return "<br><br><br><br><br><br><br><br><br><h1>No Results No Results Please check after sometime</h1>"
    except Exception as E:
        return "<br><br><br><br><br><br><br><br><br><h1>{}</h1>".format(E)

@app.route('/Education')
def Education():
    title,photo,url=[],[],[]
    def get_articles(file):
        for i in range(len(file)):
            title.append(file[i]['title'])
            photo.append(file[i]['urlToImage'])
            url.append(file[i]['url'])

    f_url='https://newsapi.org/v2/everything?'

    api_key='api key'

    perameters={
        'q':'school',
        'pagesize':100,
        'apiKey' : api_key,
        'language' : 'en',
        'from' : date.today()
    }

    response=requests.get(f_url,params=perameters)
    response_json = response.json()
    get_articles(response_json['articles'])

    def bind(url,photo,title):
            binded_list=[]
            for i in range(0,len(url),3):
                try:
                    t,ls=0,[]
                    k = i
                    while t < 3:
                        ls.append(url[k+t])
                        ls.append(photo[k+t])
                        ls.append(title[k+t])
                        t+=1
                    binded_list.append(ls)
                except:
                    return binded_list

    bils=bind(url,photo,title)
    """for i in range(len(bils)):
        if bils[i][2] != None:
            bils[i][2] = transulator.translate(bils[i][2],dest='hi').text
        if bils[i][5] != None:
            bils[i][5] = transulator.translate(bils[i][5],dest='hi').text
        if bils[i][8] != None:
            bils[i][8] = transulator.translate(bils[i][8],dest='hi').text
        """

    try:
        if bils != []:
            return render_template('Education_tab.html',ls=bils)
        else:
            return "<br><br><br><br><br><br><br><br><br><h1>No Results No Results Please check after sometime</h1>"
    except Exception as E:
        return "<br><br><br><br><br><br><br><br><br><h1>{}</h1>".format(E)


@app.route('/Entertainment')
def Entertaimnent():
    title,photo,url=[],[],[]
    def get_articles(file):
        for i in range(len(file)):
            title.append(file[i]['title'])
            photo.append(file[i]['urlToImage'])
            url.append(file[i]['url'])

    f_url='https://newsapi.org/v2/everything?'

    api_key='api key'

    perameters={
        'q':'movie',
        'pagesize':100,
        'apiKey' : api_key,
        'language' : 'en',
        'from' : date.today()
    }

    response=requests.get(f_url,params=perameters)
    response_json = response.json()
    get_articles(response_json['articles'])

    def bind(url,photo,title):
            binded_list=[]
            for i in range(0,len(url),3):
                try:
                    t,ls=0,[]
                    k = i
                    while t < 3:
                        ls.append(url[k+t])
                        ls.append(photo[k+t])
                        ls.append(title[k+t])
                        t+=1
                    binded_list.append(ls)
                except:
                    return binded_list

    bils=bind(url,photo,title)
    """for i in range(len(bils)):
        if bils[i][2] != None:
            bils[i][2] = transulator.translate(bils[i][2],dest='hi').text
        if bils[i][5] != None:
            bils[i][5] = transulator.translate(bils[i][5],dest='hi').text
        if bils[i][8] != None:
            bils[i][8] = transulator.translate(bils[i][8],dest='hi').text
        """

    try:
        if bils != []:
            return render_template('Entertaimnent_tab.html',ls=bils)
        else:
            return "<br><br><br><br><br><br><br><br><br><h1>No Results Please check after sometime</h1>"
    except Exception as E:
        return "<br><br><br><br><br><br><br><br><br><h1>{}</h1>".format(E)


@app.route('/Search',methods=['GET','POST'])
def Search():
    try:
        if request.method == 'POST':
            session['Search_Query'] = request.form['Ip']
            session['Search_list'] = list(map(str,session['Search_Query'].split(" ")))

            def search(Search_Query):
                title,photo,url=[],[],[]
                def get_articles(file):
                    for i in range(len(file)):
                        title.append(file[i]['title'])
                        photo.append(file[i]['urlToImage'])
                        url.append(file[i]['url'])

                f_url='https://newsapi.org/v2/everything?'

                api_key='api key'

                perameters={
                    'q': Search_Query,
                    'pagesize':100,
                    'apiKey' : api_key,
                    'language' : 'en',
                    'from' : date.today()
                }

                response=requests.get(f_url,params=perameters)
                response_json = response.json()
                get_articles(response_json['articles'])

                def bind(url,photo,title):
                        binded_list=[]
                        for i in range(0,len(url),3):
                            try:
                                t,ls=0,[]
                                k = i
                                while t < 3:
                                    ls.append(url[k+t])
                                    ls.append(photo[k+t])
                                    ls.append(title[k+t])
                                    t+=1
                                binded_list.append(ls)
                            except:
                                return binded_list

                bils=bind(url,photo,title)
                return bils
            merge_list=[]
            for S in session['Search_list'][-1::-1]:
                Search_res_of_split = search(S)
                if Search_res_of_split != None:
                    merge_list+=search(S)

            if merge_list != None and merge_list != []:
                return render_template('Search_tab.html',ls=merge_list)
            else:
                return render_template("no_results.html")

    except:
        return render_template("no_results.html")

    else:
        return render_template('Search.html')



@app.route('/Sports')
def Sports():
    title,photo,url=[],[],[]
    def get_articles(file):
        for i in range(len(file)):
            title.append(file[i]['title'])
            photo.append(file[i]['urlToImage'])
            url.append(file[i]['url'])

    f_url='https://newsapi.org/v2/everything?'

    api_key='api key'

    perameters={
        'q':'Sports',
        'pagesize':100,
        'apiKey' : api_key,
        'language' : 'en',
        'from' : date.today()
    }

    response=requests.get(f_url,params=perameters)
    response_json = response.json()
    get_articles(response_json['articles'])

    def bind(url,photo,title):
            binded_list=[]
            for i in range(0,len(url),3):
                try:
                    t,ls=0,[]
                    k = i
                    while t < 3:
                        ls.append(url[k+t])
                        ls.append(photo[k+t])
                        ls.append(title[k+t])
                        t+=1
                    binded_list.append(ls)
                except:
                    return binded_list

    bils=bind(url,photo,title)
    """for i in range(len(bils)):
        if bils[i][2] != None:
            bils[i][2] = transulator.translate(bils[i][2],dest='hi').text
        if bils[i][5] != None:
            bils[i][5] = transulator.translate(bils[i][5],dest='hi').text
        if bils[i][8] != None:
            bils[i][8] = transulator.translate(bils[i][8],dest='hi').text"""


    try:
        if bils != []:
            return render_template('Sports_tab.html',ls=bils)
        else:
            return "<br><br><br><br><br><br><br><br><br><h1>No Results No Results Please check after sometime</h1>"
    except Exception as E:
        return "<br><br><br><br><br><br><br><br><br><h1>{}</h1>".format(E)


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
