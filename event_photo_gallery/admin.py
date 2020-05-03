from flask import request, abort, render_template, redirect, url_for, current_app, Blueprint, flash
from flask_login import current_user
from .models import User, Category

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.before_request
def check_auth():
    if not current_user.is_authenticated:
        abort(401)
    elif not current_user.admin:
        abort(403)

@admin.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form["action"] == "add_category":
            pass
        elif request.form["action"] == "add_user":
            pass
    users = User.query.all()
    categories = Category.query.all() 
    return render_template('pages/admin.html', users=users, categories=categories)
