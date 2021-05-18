from flask import Flask
from flask_restful import Api, Resource
from firebase_admin import credentials, initialize_app, db
import views, models, resources

app = Flask(__name__)
api = Api(app)

# Initialize Firestore DB
cred_obj = credentials.Certificate('cred.json')
default_app = initialize_app(cred_obj, {
	'databaseURL':'https://spotifyparty-a6660-default-rtdb.firebaseio.com/'
	})
db = db.reference("/")




api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

if __name__ == '__main__':
    app.run(debug=True)

