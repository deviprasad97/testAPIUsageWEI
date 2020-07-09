from datetime import datetime
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class internal_user(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    user_type = db.Column(db.Integer)
    email = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    department = db.Column(db.String(64),index=True)
    password_hash = db.Column(db.String(128))
    def __repr__(self):
        return '<User %r>' % (self.email)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return internal_user.query.get(int(id))

class customer(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    fname = db.Column(db.String(64), index=True, unique=False)
    lname = db.Column(db.String(64), index=True, unique=False)
    gender = db.Column(db.Integer)
    address = db.Column(db.String(64), index=True, unique=False)
    state = db.Column(db.String(2), index=True, unique=False)
    city = db.Column(db.String(64), index=True, unique=False)
    zip = db.Column(db.String(5), index=True, unique=False)
    date_of_birth =db.Column(db.DateTime)
    # fishing, runing , bicyling, jogging
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<customer %r>' % (self.fname)

@login.c_loader
def load_c(id):
    return customer.query.get(int(id))