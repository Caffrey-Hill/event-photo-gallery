#!/bin/bash
export FLASK_ENV=development
export FLASK_APP=event_photo_gallery
export EVENT_PHOTO_GALLERY_SETTINGS=../dev.cfg

trap cleanup INT

cleanup() {
  rm -f ./dev.db
}

flask init-db
flask create-admin
flask run
