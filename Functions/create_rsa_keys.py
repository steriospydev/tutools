from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
"""
    Requirements:
        pycryptodome
"""
# Generate RSA keys

key = RSA.generate(2048) # generate private and public keys

private_key = key.export_key()

with open('private.pem', 'wb') as f:
    f.write(private_key)

public_key = key.publickey().export_key()

with open('public.pem', 'wb') as f:
    f.write(public_key)
    