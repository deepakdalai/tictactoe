from flask_restful import Resource
from flask import request 
from validators.user import validate_user
from dao.user import get_user_by_id, get_all_user, get_user_by_mail, create_user
from views import user as userview
from dao.session import get_session

class User(Resource):

    def get(self, user_id = None):
        params = request.args.to_dict()
        
        session = get_session(params['token'])
        current_user = session['user']
        
        print "\nCURRENT USER : ", get_user_by_id(current_user), "\n\n"

        if user_id:
            user = get_user_by_id(user_id)

            if not user:
                return {"response" : "User not found"}, 404  
            return {"response" : userview.single(user) }

        users = get_all_user()
        return {"response" : userview.multiple(users) }


    def post(self):
        payload = request.json
        if not validate_user(payload):
            return {"response" : "Bad request"}, 401    

        email = payload['email']
        user = get_user_by_mail(email)
        if user:
            return {"response" : "Email already used"}, 401

        create_user(payload)
        user = get_user_by_mail(email)
        return userview.single(user)
