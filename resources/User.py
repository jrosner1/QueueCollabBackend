from flask_restful import fields, marshal_with, reqparse, Resource

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'email' , dest='email',
    location='form', required=True,
    help='The user\'s username'
)
post_parser.add_argument(
    'display_name', dest='display_name',
    location='form', required=True,
    help='the user\'s display name'
)
post_parser.add_argument(
    'password', dest='password',
    
)
post_parser.add_argument(
    'email_verified', dest='email_verified',
    loation='form', required=True,
    help='Describes whether or not the user\'s email has been verified.'
)

user_fields = {
    'email': fields.String,
    'display_name': fields.String,
    'password': fields.String,
    'email_verified': fields.Boolean,
    'phone_number': fields.String
}



class User(Resource):
    @marshal_with(user_fields)
    def post(self):
        
    def get(self):
        #Method to be added
        pass
    def post(self):
        #Method to be added
        pass

