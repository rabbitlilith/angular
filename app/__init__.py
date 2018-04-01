# coding:utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ditto9689a@localhost:3306/newslistdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 
db = SQLAlchemy(app)
from app import models,views