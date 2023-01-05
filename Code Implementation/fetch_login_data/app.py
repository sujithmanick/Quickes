from flask import Flask,request,render_template,redirect,url_for,session,make_response,Response
   
app=Flask(__name__)

@app.route('/')
def index():
    try:
        if request.cookies.get("User_id") != None:
            resp = make_response(render_template('home.html',log="#",Q = request.cookies.get("User_id")))  
            return resp  
        else:
            return render_template('home.html',log="/login",Q="Login")
        
    except:
        return render_template('home.html',log="/login",Q="Login")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usr_id = request.form['email']
        Pass = request.form['psw']
        return redirect(url_for('index'))
        
    else:
        return render_template('login.html')


@app.route('/reg',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        usr_id = request.form['email']
        Pass = request.form['psw']
        psw_repeat = request.form['psw-repeat']
        try:
            print(usr_id)
            res = make_response(redirect(url_for('index')))  
            res.set_cookie('User_id',usr_id,60*60*24*365) 
            res.set_cookie('Password',Pass,60*60*24*365) 
            print("Cookie Set")
            return res
        except:
            print("cookie not set")
        
    else:
        return render_template('reg.html')



if __name__ == '__main__':
    app.run()

