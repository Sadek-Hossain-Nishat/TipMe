from flask import Flask, render_template
import os

app = Flask(__name__)

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

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500

if __name__=='__main__':
    app.run()
