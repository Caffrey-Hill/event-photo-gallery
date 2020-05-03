from flask_login import UserMixin
from . import login, db

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    passcode = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    photos = db.relationship('Photo', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    votes = db.relationship('Vote', backref='user', lazy=True)

class Photo(db.Model):
    
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80), unique=True, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                      nullable=False)
    comments = db.relationship('Comment', backref='photo', lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    votes = db.relationship('Vote', backref='photo', lazy=True)

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False) 
    photos = db.relationship('Photo', backref='category', lazy=True)

class Vote(db.Model):

    __tablename__ = 'votes'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'), primary_key=True)
    rank = db.Column(db.Integer, nullable=False)

class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photos_id = db.Column(db.Integer, db.ForeignKey('photos.id'), nullable=False)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
