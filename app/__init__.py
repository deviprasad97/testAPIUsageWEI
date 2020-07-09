from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
application = app # For beanstalk
app.config.from_object(Config)

app.secret_key = 'fegrweiugwoibgpiw40pt8940gtbuorwbgo408bg80pw4'
app.config['SESSION_TYPE'] = 'filesystem'

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
