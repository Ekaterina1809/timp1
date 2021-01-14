from flask import Flask, render_template, request, abort, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from config import Configuration
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from contextlib import closing

mysql = MySQL()
app=Flask(__name__)
#app.config.from_object(Configuration)
#db=SQLAlchemy(app)

import mysql.connector
from mysql.connector import Error

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
        if conn.is_connected():
            print('Connected to MySQL database')
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
                cursor.execute("INSERT INTO client (id_client ,login,password,fio,phone,type)",
                               (0, login, password,fio,phone,type))
                # исполняем SQL-запрос
                #cursor.execute(sql)
                # применяем изменения к базе данных
                conn.commit()
                conn.close()
                return redirect(url_for('Katalog'))
    return render_template('Rega.html')

@app.route('/Vhod')
def login():
    return render_template('Vhod.html')

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