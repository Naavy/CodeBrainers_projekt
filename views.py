from flask import render_template

from . import app
from .models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/users/')
def users():
    user_list = User.select().order_by(User.email)
    return render_template('users.html', user_list=user_list)
