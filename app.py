from flask import Flask, render_template, request, flash,redirect,url_for
import os
import mysql.connector

app = Flask(__name__)

picFolder = os.path.join('static', 'uploads')

app.config['UPLOAD_FOLDER'] = picFolder


# ginja filters e.g {{ username|striptags }}
# safe
# capitalize
# lower
# upper
# striptags
# trim
# title

app.secret_key = 'secret'

@app.route('/')
@app.route('/home')
def tip():
    return render_template("tipMe.html")




@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('psw')

        print(email)
        print(password)
        return redirect(url_for('tip'))
    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="1234",
    #     database="tipme"
    # )
    #
    # mycursor = mydb.cursor()
    #
    # sql = "SELECT * FROM accounts WHERE email ='"+email+"'"
    #
    # mycursor.execute(sql)

    # myresult = mycursor.fetchone()
    # print(myresult)


    return render_template("login.html")

@app.route('/register_status')
def registerStatus():
    redirect(url_for('login'))
    return render_template('registerstatus.html')

@app.route('/delete/<email>')
def deleteUser(email):
    try:
        mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="tipme"
                )

        mycursor = mydb.cursor()
        sql = "delete from accounts WHERE email ='"+email+"'"
        mycursor.execute(sql)

        mydb.commit()
        mydb.close()
        return email+'has been deleted'
    except Exception as e:
        return  f'{e}'


@app.route('/signup', methods=["GET", "POST"])
def signup():


    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('psw')

        print(email)
        print(password)

        confirm_password = request.form.get('psw-repeat')



        if password == confirm_password:
            flash('Success', 'success')
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="tipme"
            )

            mycursor = mydb.cursor()
            sql = "INSERT INTO accounts (email, password) VALUES (%s, %s)"
            val = (email, password)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                mydb.close()
                return redirect(url_for('login'))


            except Exception as e:
                flash(f'User already exists','error')
        else:
            flash('Passwords are not matched', 'error')



    return render_template("signup.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
