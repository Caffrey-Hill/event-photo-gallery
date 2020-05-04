import os

SECRET_KEY = os.urandom(16)
ALLOWED_PHOTO_EXTENSIONS = ['gif','jpg','jpeg','png','svg']
UPLOADS_FOLDER = 'uploads'
DISABLE_COMMENTS = False
DISABLE_VOTES = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
