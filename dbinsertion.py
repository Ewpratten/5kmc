import pymongo
import fire
import json
from usergen import genUser

# Config
MONGO_TYPE="mongodb+srv://"
MONGO_URI = "5kcluster-badue.gcp.mongodb.net/test?retryWrites=true&w=majority"
MONGO_USER = "pluginUser"

def main(user_count, password):
    
    # Connect to DB
    print("Connecting to DB")
    db = pymongo.MongoClient(f"{MONGO_TYPE}{MONGO_USER}:{password}@{MONGO_URI}")["FiveCoreDB"]["testplayers"]
    
    
    # Run through user count
    print("Adding users")
    for _ in range(user_count):
        # Get user
        userinfo:dict = json.loads(genUser())
        
        print("Adding user: " + userinfo["uuid"])
        
        # Insert a user
        db.insert_one(userinfo)
    

if __name__ == "__main__":
    fire.Fire(main)