from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from . import app, db
from .models import User, Photo

@app.errorhandler(404)
def page_not_found(e):
    return render_template("pages/404.html")

@app.errorhandler(401)
def unauthorized(e):
    return render_template("pages/401.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('photos.view_gallery'))
    elif request.method == 'POST':
        user = User.query.filter_by(passcode=request.form['passcode']).first()
        if user:
            login_user(user)
            return redirect(url_for('login'))
        else:
            flash("Invalid passcode.")
            return redirect(url_for('login'))

    else:
        return render_template('pages/login.html')
