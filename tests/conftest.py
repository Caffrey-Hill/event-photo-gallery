import os
import tempfile

import pytest

from event_photo_gallery import create_app
from event_photo_gallery.models import db

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")

@pytest.fixture
def app():
    """ A test instance of the app for each test """
    db_fd, db_path = tempfile.mkstemp()

    config = {
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + db_path,
        'TESTING': True
    }
    app = create_app(config)
    with app.app_context():
        db.create_all()
        for line in _data_sql.split("\n"):
            db.engine.execute(line)
    yield app
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """ Test client """
    return app.test_client()
