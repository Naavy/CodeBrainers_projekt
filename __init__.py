from flask import Flask
from playhouse.flask_utils import FlaskDB
from flask_admin import Admin
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db_wrapper = FlaskDB(app)
admin = Admin(app, name='Projekt bazowy', template_mode='bootstrap3')

from . import views, models
