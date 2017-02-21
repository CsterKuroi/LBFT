from time import sleep
from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain

def get():
        # Cryptographic Identities Generation
    alice, bob = generate_keypair(), generate_keypair()
    print(" ")
    # Digital Asset Definition (e.g. bicycle)
    asset = Asset(data={"bicycle": {"manufacturer":  "bkfab" ,"serial_number":  "abcd1234"}})

    # Metadata Definition
    metadata = {'planet': 'earth'}

    # create trnsaction  TODO : owners_before might be node_pubkey in v0.8.0
    tx = Transaction.create([alice.public_key], [alice.public_key], metadata = metadata, asset = asset)

    # sign with private key
    tx = tx.sign([alice.private_key])
    # get tx by id
    b = Bigchain()
    
    block = b.create_block([tx])
    block_voters = block.to_dict()['block']['voters']
    print(block_voters)
    tx_id = '2cb004cad29c0b79872646558f8c867a4c0aecbc4997f0917'    
    tx = b.get_transaction(tx_id)
    print("block status         : ",b.block_election_status('2257384a0cee8cf98bd82c3142dd38eee5c268c124b5b357b773b8c6c1fa1221',block_voters))

if __name__=='__main__':
    get()
    
