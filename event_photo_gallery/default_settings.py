import os

SITE_TITLE = 'Event Photo Gallery'
SECRET_KEY = os.urandom(16)
ALLOWED_PHOTO_EXTENSIONS = ['gif','jpg','jpeg','png','svg']
UPLOADS_FOLDER = "/".join([os.path.dirname(__file__), 'uploads'])
SQLALCHEMY_TRACK_MODIFICATIONS = False
