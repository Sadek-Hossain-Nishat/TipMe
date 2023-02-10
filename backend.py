import mysql.connector

class MySqlConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="tipme"
            )



        self.dataCursor = self.connection.cursor()

    def signUp(self,email,password):

        sql = "INSERT INTO accounts (email, password) VALUES (%s, %s)"
        val = (email, password)
        self.dataCursor.execute(sql,val)
        self.commitSqlandcloseDB()


    def logIn(self,email,password):
        try:
            sql = 'select * from accounts where email = %s'
            val=(email,)
            self.dataCursor.execute(sql,val)
            row = self.dataCursor.fetchone()

            self.commitSqlandcloseDB()
            print(row[1])
            if row[1]==password:
                return True
            else:
                return False

        except Exception as e:
            return None





    def deleteAccount(self,email):
        try:

            sql = "delete from accounts WHERE email ='" + email + "'"
            self.dataCursor.execute(sql)

            self.commitSqlandcloseDB()
            return email + 'has been deleted'
        except Exception as e:
            return  f'{e}'

    def allUsers(self):
        pass
    def selectedUser(self):
        pass
    def commitSqlandcloseDB(self):
        self.connection.commit()
        self.connection.close()