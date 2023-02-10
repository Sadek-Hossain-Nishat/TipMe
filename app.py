from flask import *
import os
from backend import MySqlConnection
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secretkey'
picFolder = os.path.join('static','uploads')

app.config['UPLOAD_FOLDER'] = picFolder

#ginja filters e.g {{ username|striptags }}
#safe
#capitalize
#lower
#upper
#striptags
#trim
#title

@app.route('/')
@app.route('/home')
def tip():
    return render_template("tipMe.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('psw')

        response =MySqlConnection().logIn(email,password)
        if response:
            return redirect(url_for('next1'))
        else:
            flash('Password is incorrenct','error')
    return render_template("login.html")

@app.route('/next1')
def next1():
    return render_template("next1.html")

@app.route('/next2')
def next2():
    return render_template("next2.html")

@app.route('/next3')
def next3():
    return render_template("next3.html")



@app.route('/delete/<email>')
def deleteUser(email):
    response = MySqlConnection().deleteAccount(email)
    return response


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('psw')

        confirm_password = request.form.get('psw-repeat')

        if password == confirm_password:
            try:
                MySqlConnection().signUp(email,password)

                return redirect(url_for('next1'))
            except:
                flash('User already exists', 'error')

        else:
            flash('Passwords are not matched','error')

    return render_template("signup.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500

if __name__=='__main__':
    app.run(debug=True)
