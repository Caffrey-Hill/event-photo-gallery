from flask import request, abort, render_template, redirect, url_for, current_app, Blueprint, flash
from flask_login import current_user
from .models import db, User, Category, Photo, Vote
from .login import generate_passcode

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.before_request
def check_auth():
    if not current_user.is_authenticated:
        abort(401)
    elif not current_user.admin:
        abort(403)

@admin.route('/')
def index():
    stats = {
        'users': User.query.count(),
        'categories': Category.query.count(),
        'votes': Vote.query.count(),
        'photos': Photo.query.count(),
    }
    return render_template('pages/admin/index.html', **stats)

@admin.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == "POST":
        if request.form["action"] == "add":
            user = User(name=request.form["name"], passcode=generate_passcode())
            db.session.add(user)
            db.session.commit()
        elif (request.form["action"] == "delete" and 
                current_user.id != request.form["id"]):
            user = User.query.filter_by(id=request.form["id"]).first()
            if user:
                db.session.delete(user)
                db.session.commit()
            else:
                abort(400)
        else:
            abort(400)
    users = User.query.all()
    return render_template('pages/admin/users.html', users=users)

@admin.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == "POST":
        if request.form["action"] == "add":
            category = Category(name=request.form["name"])
            db.session.add(category)
            db.session.commit()
        elif request.form["action"] == "edit":
            category = Category.query.filter_by(id=request.form["id"]).first()
            if category:
                category.voting_enabled = True if 'voting_enabled'\
                        in request.form else False
                category.comments_enabled = True if 'comments_enabled'\
                        in request.form else False
                category.uploads_enabled = True if 'uploads_enabled'\
                        in request.form else False
                category.name = request.form["name"]
                db.session.commit()
            else:
                abort(404)
        elif request.form["action"] == "delete":
            category = Category.query.filter_by(id=request.form["id"]).first()
            if category:
                db.session.delete(category)
                db.session.commit()
            else:
                abort(404)
        else:
            abort(400)

    categories = Category.query.all()
    return render_template('pages/admin/categories.html', categories=categories)
