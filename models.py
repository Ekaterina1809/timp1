from flask_login import UserMixin

from config import db, login_manager
#from route import db, login_manager

class client(db.Model, UserMixin):
    id_client = db.Column(db.Integer, primary_key=True, unique=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    fio = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, default=0)
    type = db.Column(db.String, nullable=False, default=0)


'''class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    team_1 = db.Column(db.Boolean, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ended = db.Column(db.Boolean, nullable=False, default=False)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_1 = db.Column(db.Integer, nullable=False)
    team_2 = db.Column(db.Integer, nullable=False)
    bets = db.relationship('Bet', backref='event', lazy=True)
    amount1 = db.Column(db.Integer, nullable=False, default=0)
    amount2 = db.Column(db.Integer, nullable=False, default=0)
    time = db.Column(db.DateTime, nullable=False)
    ended = db.Column(db.Boolean, nullable=False, default=False)
    winner = db.Column(db.Boolean, nullable=True)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    avatar_uri = db.Column(db.String(128))
    # events = db.relationship('Event', backref='teams', lazy=True)
'''

@login_manager.user_loader
def load_client(login):
    return client.query.get(login);
