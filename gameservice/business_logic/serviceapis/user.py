from flask_restful import Resource
from flask import request 
from validators.user import validate_user
from dao.user import get_user_by_id, get_all_user 
from views import user as userview

class User(Resource):

    def get(self, user_id = None):
        if user_id:
            user = get_user_by_id(user_id)
            if not user:
                return {"response" : "User not found"}, 404  
            return {"response" : userview.single(user) }

        params = request.args.to_dict()
        if params:
            #handle params
            return {"response" : get_users_by_params(params)}
        else:
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
