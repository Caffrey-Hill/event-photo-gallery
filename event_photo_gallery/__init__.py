from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('event_photo_gallery.default_settings')
    app.config.from_envvar('EVENT_PHOTO_GALLERY_SETTINGS')

    from .models import db, User
    db.init_app(app)

    from .login import generate_passcode, login
    login.init_app(app)

    from .public import public
    from .admin import admin
    from .photos import photos

    app.register_blueprint(public)
    app.register_blueprint(photos)
    app.register_blueprint(admin, url_prefix='/admin')

    with app.app_context():
        db.create_all()
    
        admins = User.query.filter_by(admin=True).all()
        if not any(admins):
            passcode = generate_passcode()
            user = User(name="admin", passcode=passcode, admin=True)
            print('No admin users found. Created admin passcode: %s' % (passcode))
            db.session.add(user)
            db.session.commit()

    return app
