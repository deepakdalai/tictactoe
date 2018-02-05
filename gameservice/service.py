from flask import Flask
from flask_restful import Resource, Api
from business_logic.serviceapis.ping import Ping
from business_logic.serviceapis.user import User
from business_logic.serviceapis.validation import UserValidation

from flask import request 


app = Flask(__name__)
api = Api(app)


api.add_resource(Ping, '/ping/')
api.add_resource(User, '/user','/user/<string:user_id>')
api.add_resource(UserValidation, '/uservalidation')


#api.add_resource(GameInstance, '')
#api.add_resource(Move,)



if __name__ == '__main__':
    app.run(debug=True)
