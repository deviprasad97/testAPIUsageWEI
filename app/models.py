from datetime import datetime
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, username, hash):
        self.name = username
        self.hash = hash
    
    @property
    def id(self):
        return self.name

# class Admin(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     phone = db.Column(db.String(10))
#     department = db.Column(db.String(64))
#     usertype =db.Column(db.Integer)

#     def __repr__(self):
#         return '<Admin {}>'.format(self.username)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.id


# class Customer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(64), index=True, unique=True)
#     phone = db.Column(db.String(10), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     fname = db.Column(db.String(64), index=True, unique=False)
#     lname = db.Column(db.String(64), index=True, unique=False)
#     gender = db.Column(db.Integer)
#     address = db.Column(db.String(64))
#     state = db.Column(db.String(2))
#     city = db.Column(db.String(64))
#     zip = db.Column(db.String(5))
#     score = db.Column(db.Integer, index=True, unique=False)
#     date_of_birth = db.Column(db.DateTime)

#     def __repr__(self):
#         return '<Customer {}>'.format(self.username)
    
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)


#custmer system need use this and disable the admin.@login.user_loader.
#@login.user_loader     
#def load_user(id):
#    return Customer.query.get(int(id))    