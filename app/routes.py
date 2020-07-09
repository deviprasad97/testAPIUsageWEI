from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm, RegistrationForm
from app.models import Admin, Customer, User
import requests
from flask_session import Session
from flask import session


sess = Session()
sess.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    if 'user' in session:
        print('User Found')
        return render_template('index.html', data=session['user'].name)
    else:
        print('User not Found')
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    jsonPayload = None
    if form.validate_on_submit():
        jsonPayload = {
                'username':form.username.data,
                'password':form.password.data
            }
        result = requests.post('http://ec2-34-212-133-20.us-west-2.compute.amazonaws.com/auth/login', json=jsonPayload)

        result = result.json()
        if result['status'] != 'fail':
            user = User(form.username.data, result['auth_token'])
            login_user(user)
            session['user'] = user
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    session.pop('user', None)
    return redirect(url_for('index'))


# @app.route('/register', methods=['GET', 'POST'])
# @login_required
# def register():
    
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = Admin(username=form.username.data, email=form.email.data, phone=form.phone.data,department=form.department.data, usertype=int(form.usertype.data))
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you registered a new user for the system!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)


# @app.route('/view')
# @login_required
# def view():
#     customers = Customer.query.all()
#     return 'render_template('
    
