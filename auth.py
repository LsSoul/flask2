from flask import Blueprint,render_template,redirect, url_for, request, flash
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required
import time
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/login', methods=['POST'])
def login_post():
    mail = request.form.get('mail')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(mail=mail).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('auth.logged'))

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('name')
    mail = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(mail=mail).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.register'))

    new_user=User(username=username, password=generate_password_hash(password, method='sha256'), mail=mail)
                        

    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/logged')
@login_required
def logged():
    return render_template('logged.html')

@auth.route('/logged', methods=['POST'])
@login_required
def logged_post():
    device_id = request.form.get('device_id')
    f = open('./flaskproj/static/images/device_id.txt','w')
    f.write(str(device_id))
    f.close()
    time.sleep(1)
    return redirect(url_for('auth.logged'))
@auth.route('/quisom')
def quisom():
    return render_template('quisom.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
