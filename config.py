from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from hashlib import sha256

# соль
salt = 'qwerty123'
# пароль администратора
#admin_password = 'admin'

app = Flask(__name__, static_folder='static')
app.secret_key = salt
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://postgres:postgres@bets-db:5432'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
#login_manager = LoginManager(app)

TIME_FORMAT = '%Y-%m-%dT%H:%M'

#import models
#import app

#db.create_all()

