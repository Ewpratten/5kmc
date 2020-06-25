import json
import random
import uuid
from ipaddressutil import generateRealisticIPAddr
from date import randISODate, randUNIXDate

def createRandomPunishment() -> dict:
    
    # types
    types:list = json.load(open("schema/punishment_types.json"))
    
    # Pick a random type
    randType:str = random.choice(types)
    
    return createPunishment(randType)
    
def createPunishment(punishType:str) -> dict:
    
    # Load punishment schema
    schema:dict = json.load(open("./schema/punishment.json"))
    
    # Fill in enforcer
    schema["enforcer"] = str(uuid.uuid1())
    
    # Fill in creation time
    schema["created_at"] = randISODate()
    
    # Decide if an expiry should be generated
    shouldGenExpiry = random.randint(0,1) == 1
    
    if shouldGenExpiry:
        schema["expires_at"] = randISODate()
    else:
        del schema["expires_at"]

    # If this is an ipban, add an IP
    if punishType == "ipban":
        schema["ip"] = generateRealisticIPAddr()
    else:
        del schema["ip"]
    
    # Fill in type
    schema["type"] = punishType
    
    # Fill in message
    schema["message"] = "THIS PUNISHMENT IS AUTO-GENERATED"
    
    return schema