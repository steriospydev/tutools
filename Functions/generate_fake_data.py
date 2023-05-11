import re
from faker import Faker
"""
Requirements:
    faker
"""

def generate_data(lang:str, no_items:int) -> dict:
    faker = Faker(lang)    
    info =[]

    names = [faker.unique.name() for i in range(no_items)]
    addresses = [ re.sub("\n", "", faker.unique.address()) for i in range(no_items)]
    for i in range(0, no_items):
        info.append({
            'name': names[i],
            'address' :  addresses[i]
            })
    return info


