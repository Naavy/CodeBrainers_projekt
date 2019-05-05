from flask import Flask
from playhouse.flask_utils import FlaskDB
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db_wrapper = FlaskDB(app)

from . import views, models
