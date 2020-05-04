event-photo-gallery: A collaborative, micro photo gallery
==================================================

:Site:  https://github.com/ReverentEngineer/event-photo-gallery
:Original author: Jeff Caffrey-Hill <jeff@reverentengineer.com>

.. contents::
   :local:

event-photo-gallery is a `Flask <https://palletsprojects.com/p/flask/>`_-based 
micro photo gallery that is designed to enable users to create a small space
for their guests to share and view photos.

Requirements
------------

Required packages include: Flask, Flask-SQLAlchemy, Flask-Login,pillow, and piexif

How to run
-------------

If you're using gunicorn for your production server, you can run::

  gunicorn event_photo_gallery:app

If you're using uswgi for your production server, you can run::

  uwsgi --socket 0.0.0.0:5000 --protocol=http -w event_photo_gallery:app

Configuration file
-------------------

To configure your instance, you need to create a config file in python and
set the environment variable EVENT_PHOTO_GALLERY_SETTINGS to it's location.

An example configuration file.

.. code-block:: python

  SITE_TITLE="My site"
  SITE_SUBTITLE="My subtitle"
  SQLALCHEMY_DATABASE_URI="sqlite:////var/lib/mysite/site.db"
  SECRET_KEY="39238ebacc4e2e83c6d9c32add2516c6"
  UPLOADS_FOLDER="/var/lib/mysite/uploads"
