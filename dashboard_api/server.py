# encoding: utf-8
"""Application.

Starts the Flask application
"""

from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from resources.user import Users

api = Api(app)
api.add_resource(Users, '/users')
db.create_all()