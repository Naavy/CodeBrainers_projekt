import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qmRMwl04YpAXu6inWQ89'
    DATABASE = (
        os.environ.get('DATABASE_URL')
        or
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
