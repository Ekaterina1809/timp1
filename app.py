from flask import Flask, render_template, request, abort, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from contextlib import closing
from hashlib import sha256
from config import (salt)

mysql = MySQL()
app=Flask(__name__)
#app.config.from_object(Configuration)
#db=SQLAlchemy(app)

import mysql.connector
from mysql.connector import Error

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('Vhod') + '?next=' + request.url)
    return response

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='timp',
                                       user='root',
                                       password='1809')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)
    return connect()

 #   finally:
#        conn.close()


# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = '1809'
#app.config['MYSQL_DATABASE_DB'] = 'timpBD1'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Rega',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        phone = request.form.get('number')
        fio = request.form.get('namefam')
        password = request.form.get('psw')
        password2 = request.form.get('psw-repeat')
        type = request.form.get('num-lico')

        # All Good, let's call MySQL
        conn = mysql.connector.connect(host='localhost',
                                       database='timp',
                                       user='root',
                                       password='1809')
        #if conn.is_connected():
        #fr    print('Connected to MySQL database')
        cursor = conn.cursor()  # используя метод cursor() получаем объект для работы с базой
        #conn = mysql.connect()

        #_hashed_password = generate_password_hash(password)
        #cursor.callproc('client', (login, password, _hashed_password))
        #data = cursor.fetchall()

        if login and password and password2:
            if not (login and password and password2):
                flash('Please fill all fields')
            elif password != password2:
                flash('Passwords are not equal!')
            #elif client.query.filter_by(login=login).first():
             #   flash('Login is busy')
            else:
                #password = sha256((password + salt).encode()).hexdigest()
                # формируем sql запрос на запись
                sql="INSERT INTO client (id_client ,login,password,fio,phone,type) VALUES (%s, %s,%s, %s,%s, %s)"
                val =(0, login, password,fio,phone,type)
                # исполняем SQL-запрос
                cursor.execute(sql,val)
                # применяем изменения к базе данных
                conn.commit()
                conn.close()
                return redirect(url_for('Katalog'))
    return render_template('Rega.html')

@app.route('/Katalog')
def Katalog():
    return render_template('Katalog.html')

@app.route('/Vhod',methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            login = request.form.get('login')
            password = request.form.get('password')
            if login and password:
                #user = User.query.filter_by(login=login).first()
                #password = sha256((password + salt).encode()).hexdigest()
                if user and user.password == password:
                    #login_user(user)
                    next_page = request.args.get('next')
                    if next_page:
                        return redirect(next_page)
                    return redirect(url_for('index'))
                else:
                    flash('Incorrect login or password')
            else:
                flash('Please enter login and password')
        return render_template('Vhod.html')

#@app.route('/logout', methods=['GET', 'POST'])
#@login_required
#def logout():
#    logout_user()
#   return redirect(url_for('index'))

@app.route('/user/<name>')
@app.route('/user/')
def user(name=None):
    if name is None:
        name=request.args.get('name')
    if name:
        return render_template('index.html', name=name)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)