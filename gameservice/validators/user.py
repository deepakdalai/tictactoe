from jsonschema import validate

schema = {
            "type" : "object",
            "properties" : {
                "name" : {"type" : "string"},
                "email" : {"type" : "string"},
                "alias" : {"type" : "string"},
                "password" : {"type" : "string"}
            }
        }

def validate_user(payload):
    try:
        validate(payload,schema)
        return True
    except:
        return False

