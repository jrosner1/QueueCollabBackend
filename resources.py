from flask_restful import Resource, reqparse
import models
from firebase_admin import auth
from firebase_admin.auth import UserRecord


parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument("email", required=True, help="The email address of the new user to be created")
parser.add_argument("user-id", required=False,
                        help="The user id to assign to the new user. If this is not specified, "
                             "Firebase will generate a random string.")




class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        new_user = models.UserModel(
            data['username'],
            data['password']
        )
        try:
            new_user.save_to_db()
            return {
                'message' : 'User {} was created'.format(data['username'])
            }
        except:
            return {'message': 'Something when wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return {'message': 'User login'}

class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}

class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}

class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}

class AllUsers(Resource):
    def get(self):
        return {'message':'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}

class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }