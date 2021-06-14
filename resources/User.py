from flask import jsonify, request
from flask_restful import Resource
from common.firebase_util import create_user
from marshmallow import Schema, fields, post_load
from Models import UserModel

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime(required=False)
    password = fields.Str()
    phone_number = fields.Str()
    display_name = fields.Str(required=False)
    email_verified = fields.Bool(required=False)

    @post_load
    def make_user(self, data, **kwargs):
        return UserModel(**data)

class User(Resource):
    def post(self):
        schema = UserSchema(many=True)
        print(request.json)
        result = schema.load(request.json)
        result.save_to_db()



