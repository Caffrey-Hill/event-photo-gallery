from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('event_photo_gallery.default_settings')
app.config.from_envvar('EVENT_PHOTO_GALLERY_SETTINGS')

db = SQLAlchemy(app)
login = LoginManager(app)

from .models import *

db.create_all()

from .utils import generate_passcode
from .photos import photos
from .admin import admin
from .public import *

app.register_blueprint(photos, url_prefix='/photos')
app.register_blueprint(admin, url_prefix='/admin')

admins = User.query.filter_by(admin=True).all()
if not any(admins):
    passcode = generate_passcode()
    user = User(name="admin", passcode=passcode, admin=True)
    print('No admin users found. Created admin passcode: %s' % (passcode))
    db.session.add(user)
    db.session.commit()
