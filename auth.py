from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from firebase_config import auth
import json

auth_bp = Blueprint('auth', __name__)

def get_error_message(error):
 try:
    error_json = error.args[0]
    error_data = json.loads(error_json)
    error_message = error_data['error']['message']
    if error_message == 'EMAIL_NOT_FOUND':
        return 'No account found with this email. Please sign up first.'
    elif error_message == 'INVALID_PASSWORD':
        return 'Incorrect Password. Please try again.'
    elif error_message == 'EMAIL_EXISTS':
        return 'This email is already in use. Please try logging in or use a different email.'
    elif error_message == 'WEAK_PASSWORD':
        return 'The password is too weak. Please choose a stronger password.'
    else:
        return error_message
 except:
    return 'An unexpected error occurred. Please try again.'
@auth_bp.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(user['idToken'])
            flash('Please verify your email address')
            #Redirecting to login page after signing up
            return redirect(url_for('auth.login'))
        except Exception as e:
            error_message = get_error_message(e)
            flash(error_message)
            return redirect(url_for('auth.signup'))
    #return render_template('signup.html')

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            flash('Successfully Logged in!!')
            #return redirect(url_for main dashboard)
        except Exception as e:
            error_message = get_error_message(e)
            flash(error_message)
            return redirect(url_for('auth.login'))
    return render_template('login.html')

