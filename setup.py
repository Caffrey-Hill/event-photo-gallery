from setuptools import setup, find_packages
import os

def get_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
             paths.append(os.path.join('..', path, filename))
    return paths

static_files = get_files('event_photo_gallery/static')
template_files = get_files('event_photo_gallery/templates')

setup(
    name="event-photo-gallery",
    version='1.0.2',
    platforms="all",
    packages=find_packages(),
    package_data={
        "": static_files + template_files
    },
    author="Jeff Caffrey-Hill",
    author_email="jeff@reverentengineer.com",
    install_requires=(
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Login',
        'pillow',
        'piexif',
    ),
)
