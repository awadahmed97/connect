import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

#changed user awadahmed
# TODO IMPLEMENT DATABASE URL
#mysql://username:password@server/db
SQLALCHEMY_DATABASE_URI = 'postgresql://awadahmed@localhost:5432/connect'
