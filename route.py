from hashlib import sha256

from flask import Flask, render_template, request, abort, flash, url_for, redirect, g
from flaskext.mysql import MySQL

from config import (salt,db,app)
from models import (client)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import os
from functools import wraps
mysql = MySQL()

#app=Flask(__name__)
#app.config.from_object(Configuration)
#db=SQLAlchemy(app)

import mysql.connector
from mysql.connector import Error

@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next=' + request.url)
    return response

@app.before_request
def before_request():
    g.user=current_user

@app.route('/',methods=['GET'],endpoint='index')
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

        if login and password and password2:
            if not (login and password and password2):
                flash('Please fill all fields')
            elif password!= password2:
                flash('Passwords are not equal!')
            else:
                password = sha256((password + salt).encode()).hexdigest()
                new_user = client(id=0, login=login, password=password, fio=fio, phone=phone, type=type)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('Katalog'))
    return render_template('Rega.html')


@app.route('/Katalog')
@login_required
def Katalog():
    return render_template('Katalog.html')

@app.route('/Vhod',methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
            login = request.form.get('login')
            password = request.form.get('psw')
            if login and password:
                #client_login = client.query.filter_by(login=login).first()
                client_id = db.session.query(client).filter_by(login=login).count()
                clientt = db.session.query(client).filter_by(login=login).first()
                #is_exists = session.query(exists().where(login == login)).scalar()
                print(client_id)
                password = sha256((password + salt).encode()).hexdigest()
                #password_id = db.session.query(client).filter_by(password=password).count()
                password_id = db.session.query(client).filter_by(login=login,password=password).count()
                print(password_id)
                if ((client_id>0) and (password_id>0)) :
                    login_user(clientt)
                    next_page = request.args.get('next')
                    if next_page:
                        return redirect(next_page)
                    return redirect(url_for('Katalog'))
                else:
                    flash('Incorrect login or password')
        return render_template('Vhod.html')

@app.route('/Mypage')
@login_required
def Mypage():
    return render_template('Lichkab.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


'''
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
'''

# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = '1809'
#app.config['MYSQL_DATABASE_DB'] = 'timpBD1'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)
from functools import wraps
#app = Flask(__name__, static_folder='static')'''
'''def exception_handler(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        return f(args,kwargs)
    return decorator'''

''' password = sha256((password + salt).encode()).hexdigest()
                new_user = client(login=login,password = password, fio=fio, phone=phone,type=type)
                db.session.add(new_user)
                db.session.commit()'''
                #password = sha256((password + salt).encode()).hexdigest()
                # формируем sql запрос на запись

#if __name__ == '__main__':
#    app.run(debug=True)
'''conn = mysql.connector.connect(host='localhost',
                                               database='timp',
                                               user='root',
                                               password='1809')
                cursor = conn.cursor()
                sql = "SELECT login FROM client where login='login'"
                login = cursor.execute(sql)
                sql = "SELECT password FROM client where login='login'"
                #val = (0, login, password, fio, phone, type)SELECT * FROM post WHERE text LIKE 'статьи%'
                # исполняем SQL-запрос
                client_password=cursor.execute(sql)

                # применяем изменения к базе данных
                conn.commit()
                conn.close()'''

# All Good, let's call MySQL
'''conn = mysql.connector.connect(host='localhost',
                               database='timp',
                               user='root',
                               password='1809')
cursor = conn.cursor()  # используя метод cursor() получаем объект для работы с базой'''
''' sql="INSERT INTO client (id_client ,login,password,fio,phone,type) VALUES (%s, %s,%s, %s,%s, %s)"
        val =(0, login, password,fio,phone,type)
        # исполняем SQL-запрос
        cursor.execute(sql,val)
        # применяем изменения к базе данных
        conn.commit()
        conn.close()'''