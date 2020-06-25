import fire
import json
import random
from ipaddress import generateRealisticIPAddr


def genUser(currency:int = None, ip_count:int = None, punishment_count:int = None) -> dict:
    """Generates a user DB entry in JSON format"""
    
    # Calculate params
    currency:int = currency if currency is not None else random.randint(0, 1000000)
    ip_count:int = ip_count if ip_count is not None else random.randint(1, 5)
    punishment_count:int = punishment_count if punishment_count is not None else random.randint(0, 10)
    
    
    
    return {}

if __name__ == "__main__":
    fire.Fire(genUser)