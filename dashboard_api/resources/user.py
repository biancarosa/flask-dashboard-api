from flask_restful import Resource, Api

class User(Resource):

    def get(self, todo_id):
        return {}

    def put(self, todo_id):
        return {}
    
    def patch(self, todo_id):
        return {}
    
    def delete(self, todo_id):
        return {}

class Users(Resource):

    def get(self, todo_id):
        return [{}]
        
    def post(self):
        return {}
        