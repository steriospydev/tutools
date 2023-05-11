from hashlib import sha256
import time

MAX_NONCE = 100000000000000


def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    for nonce in range(MAX_NONCE):
        prefix_str = '0' * prefix_zeros
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Succesfully mined a block with nonce:{nonce}")
            return new_hash
    raise BaseException(f"Could not find correct trying {MAX_NONCE} times")


if __name__ == '__main__':
    transactions = '''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty = 3
    start = time.time()
    print("start mining...\n")
    new_hash = mine(667453, transactions, '00470320360b23bbdb7a224452593cb32a211eebfd3f1fe', difficulty)
    total_time = str((time.time() - start))
    print("\nEnd mining.\nTook:" + total_time + " seconds")
    print("\n")
    print(new_hash)