from os import environ
from flask import Flask

app = Flask(__name__)
app.config.update(SECRET_KEY=environ['FLASK_SECRET_KEY'])

from app import views
