from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import app,db

class UserList(db.Model):
    __tablename='userlist'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return '<UserList %r>' % self.username

