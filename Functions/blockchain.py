import json
import hashlib

class Block:
  id = None
  history = None
  parent_id = None
  parent_hash = None



nelson = Block()
marie = Block()
sky = Block()

nelson.id = 1
nelson.history = 'Nelson likes cats'

marie.id = 2
marie.history = 'Marie likes cat'
marie.parent_id = nelson.id
marie.parent_hash = hashlib.sha256(json.dumps(nelson.__dict__).encode('utf-8')).hexdigest()

sky.id = 3
sky.history = 'Sky hates dogs'
sky.parent_id = marie.id
sky.parent_hash = hashlib.sha256(json.dumps(marie.__dict__).encode('utf-8')).hexdigest()

# prints
print('marie.__dict__:')
print(marie.__dict__)
print('\nmarie json dumbs:')
print(json.dumps(marie.__dict__))
print('\nmarie block hash without hexdigest function')
print(hashlib.sha256(json.dumps(nelson.__dict__).encode('utf-8')))
print('\n marie block with hexdigest function')
print( hashlib.sha256(json.dumps(marie.__dict__).encode('utf-8')).hexdigest())

# New block
sky_2 = Block()
sky_2.id = 4
sky_2.history = 'Sky loves turtle'
sky_2.parent_id = sky.id

block_serialized = json.dumps(sky_2.__dict__).encode('utf-8')
print(block_serialized)