import fire
import json
import random
from ipaddressutil import generateRealisticIPAddr
from date import randISODate, randUNIXDate
import uuid
from punishments import createRandomPunishment

def genUser(currency:int = None, ip_count:int = None, punishment_count:int = None) -> dict:
    """Generates a user DB entry in JSON format"""
    
    # Calculate params
    currency:int = currency if currency is not None else random.randint(0, 1000000)
    ip_count:int = ip_count if ip_count is not None else random.randint(1, 5)
    punishment_count:int = punishment_count if punishment_count is not None else random.randint(0, 10)
    
    # Load schema
    schema:dict = json.load(open("./schema/user.json"))
    
    # Fill in uuid
    schema["uuid"] = str(uuid.uuid1())
    
    # Fill in currency
    schema["currency"] = currency
    
    # Fill in join and login times
    schema["first_joined"] = randISODate()
    schema["last_login"] = randISODate()
    
    # Fill in IP addresses
    schema["ips"] = [generateRealisticIPAddr() for _ in range(ip_count)]
    
    # Fill in punishments
    schema["punishments"] = [createRandomPunishment() for _ in range(punishment_count)]
    
    return json.dumps(schema)

if __name__ == "__main__":
    fire.Fire(genUser)