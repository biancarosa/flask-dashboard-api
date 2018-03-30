from flask import request
from flask_restful import Resource, Api
from dashboard_api.models.user import User

class Users(Resource):

    def get(self):
        users = User.query.all()
        return [dict((col, getattr(user, col)) for col in user.__table__.columns.keys()) for user in users]

        
    def post(self):
        request_data =  request.get_json()
        user = User()
        user.email = request_data.get('email')
        user.first_name = request_data.get('first_name')
        user.last_name = request_data.get('last_name')
        user.username = request_data.get('username')
        user.password = request_data.get('password')
        user.save()
        return dict((col, getattr(user, col)) for col in user.__table__.columns.keys())
        