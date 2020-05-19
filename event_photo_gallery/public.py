from flask import request, render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from .models import db, User, Photo

public = Blueprint('public', __name__, template_folder='templates')

@public.app_errorhandler(404)
def page_not_found(e):
    return render_template("pages/404.html")

@public.app_errorhandler(401)
def unauthorized(e):
    return redirect(url_for('public.login'))

@public.route('/auth')
def authenticated():
    if current_user.is_authenticated:
        return "Authenticated", 200
    else:
        return "Unauthenticated", 401

@public.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('public.login'))

@public.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('photos.view_gallery'))
    elif request.method == 'POST':
        user = User.query.filter_by(passcode=request.form['passcode']).first()
        if user:
            remember = True if 'remember' in request.form and\
                    request.form['remember'] == 'true' else False
            login_user(user, remember=True)
            return redirect(url_for('photos.view_gallery'))
        else:
            flash("Invalid passcode.")
            return redirect(url_for('public.login'))

    else:
        return render_template('pages/login.html')
