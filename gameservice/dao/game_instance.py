from pymongo import MongoClient
from bson import ObjectId
from utils import constants as gconst 

client = MongoClient()
db = client.game_engine

ginstancecltn = db.game_instance

def create_game_instance(user1_obj_id, user2_obj_id):
    instance_object = {
        "user1" : user1_obj_id,
        "user2" : user2_obj_id,
        "cstate" : gconst.default_state,
        "status" : gconst.default_start_status,
        "next_player" : user1_obj_id,
        "winner" : None
    }
    gi = ginstancecltn.insert_one(instance_object)
    return gi.inserted_id


def get_game_instance(game_obj_id):
    return ginstancecltn.find_one({"_id" : game_obj_id})

def accepted_game_instance(game_obj_id):
    ginstancecltn.update_one(
        {"_id" : game_obj_id}, 
        {"$set" : { "status" : gconst.accepted_status } })

def make_move(game_obj_id, new_state, next_player, new_status, winner = None):
    ginstancecltn.update_one(
        {"_id" : game_obj_id}, 
        {"$set" : 
            {  "cstate" : new_state,
               "status" : new_status,
               "next_player" : next_player,
               "winner" : winner}
        }
    )

if __name__ == "__main__":
    user1 = ObjectId("5a6d587f3fea99af9623c010")
    user2 = ObjectId("5a6d59533fea99b0b6bbcd8b")
    gi = create_game_instance(user1, user2)

    print "CREATED : ", get_game_instance(gi)

    accepted_game_instance(gi)
    print "ACCEPTED : ", get_game_instance(gi)

    make_move(
        gi, 
        [[None,None,"X"],[None,None,None],[None,None,None]], 
        user2, 
        gconst.accepted_status)

    print "MOVED : ", get_game_instance(gi)



    

