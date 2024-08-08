from flask import Flask, redirect,url_for
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    # return 'HELLO'
    return "Hello! This is the main page <h1>Hello World</h1>"

@app.route('/<name>')
def user(name):
    return f"Hello, {name}"

@app.route('/admin')
def admin():
    # return redirect(url_for("home"))
    return redirect(url_for("user", name="Admin !"))
  
if __name__=='__main__': 
   app.run() 
