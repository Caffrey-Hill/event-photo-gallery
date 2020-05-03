from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['ALLOWED_PHOTO_EXTENSIONS'] = ['gif','jpg','jpeg','png','svg']
app.config['UPLOADS_FOLDER'] = 'uploads'
app.config['DISABLE_COMMENTS'] = False
app.config['DISABLE_VOTES'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_envvar('EVENT_PHOTO_GALLERY_SETTINGS')

if 'SECRET_KEY' not in app.config:
    import os
    app.config['SECRET_KEY'] = os.urandom(16)

db = SQLAlchemy(app)
login = LoginManager(app)

from .models import *

db.create_all()

from .utils import generate_passcode
from .photos import photos
from .public import *

app.register_blueprint(photos, url_prefix='/photos')

admins = User.query.filter_by(admin=True).all()
if not any(admins):
    passcode = generate_passcode()
    user = User(name="admin", passcode=passcode, admin=True)
    print('No admin users found. Created admin passcode: %s' % (passcode))
    db.session.add(user)
    db.session.commit()
