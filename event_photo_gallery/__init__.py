from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    if isinstance(config, dict):
        for key in config:
            app.config[key] = config[key]
    app.config.from_object('event_photo_gallery.default_settings')
    app.config.from_envvar('EVENT_PHOTO_GALLERY_SETTINGS', silent=True)

    from .models import db
    db.init_app(app)

    from .login import generate_passcode, login
    login.init_app(app)

    from .cache import cache
    cache.init_app(app)

    from .public import public
    from .admin import admin
    from .photos import photos

    app.register_blueprint(public)
    app.register_blueprint(photos)
    app.register_blueprint(admin, url_prefix='/admin')

    from .models import init_db, create_admin
    app.cli.add_command(init_db)
    app.cli.add_command(create_admin)

    return app
