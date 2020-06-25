import random


def generateRealisticIPAddr() -> str:
    """Generate a real IP address"""
    
    # Build address
    ip = []
    ip.append(str(random.randint(0, 255)))
    ip.append(str(random.randint(0, 255)))
    ip.append(str(random.randint(0, 255)))
    ip.append(str(random.randint(0, 255)))
    
    # Join
    return '.'.join(ip)