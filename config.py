from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from hashlib import sha256
#from os import environ
#environ.get('APP_DATABASE_HOST','127.0.0.1')
# соль
salt = 'qwerty123'

app = Flask(__name__, static_folder='static')
app.secret_key=salt
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1809@127.0.0.1:3306/timp1'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.view='login'

TIME_FORMAT = '%Y-%m-%dT%H:%M'

import models
import route

db.create_all()
admin_password='nimda'
if not models.client.query.filter_by(login='admin').first():
        password = sha256((admin_password + salt).encode()).hexdigest()
        #new_user = models.client(login='admin',password=password,fio='admin',phone='0', type='0')
        #db.session.add(new_user)
        db.session.commit()