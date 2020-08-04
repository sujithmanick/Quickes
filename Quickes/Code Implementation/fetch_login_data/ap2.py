import flask  
  
app = flask.Flask(__name__)  
 
@app.route('/cookie')  
def cookie():  
    res = flask.make_response()  
    res.set_cookie('Test 1','Photos') 
    return res
    
   
  
if __name__ == '__main__':  
    app.run(debug = True)  