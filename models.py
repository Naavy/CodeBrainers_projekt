import peewee as db
from . import db_wrapper


class User(db_wrapper.Model):
    email = db.CharField(max_length=128, index=True, unique=True)
    password_hash = db.CharField(max_length=128)

    def __str__(self):
        return '<User {}>'.format(self.email)
