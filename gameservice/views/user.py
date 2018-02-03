

def single(user_object):
    return {
        "userId" : str(user_object["_id"]),
        "eMailAddress" : user_object.get("email","No Email Address"),
        "userName" : user_object.get("name","Default Name")
    }

def multiple(user_objects):
    print user_objects, "\n\n"
    return [ single(user_object) for user_object in user_objects ]