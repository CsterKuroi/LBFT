from time import sleep
from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain
from bigchaindb.models import Block

def tamper_block():
    # Cryptographic Identities Generation
    alice, bob = generate_keypair(), generate_keypair()
    
    # Digital Asset Definition (e.g. bicycle)
    asset = Asset(data={"bicycle": {"manufacturer":  "bkfab" ,"serial_number":  "abcd1234"}})

    # Metadata Definition
    metadata = {'planet': 'earth'}

    # create trnsaction  TODO : owners_before might be node_pubkey in v0.8.0
    tx = Transaction.create([alice.public_key], [alice.public_key], metadata = metadata, asset = asset)
    
    # sign with private key
    tx = tx.sign([alice.private_key])
    tx_id = tx.to_dict()['id']

    # 
    b = Bigchain()
    block = b.create_block([tx])
    block_id = block.to_dict()['id']
    
    block.timestamp = '1'
    print(block.to_dict())
    b.write_block(block)

if __name__=='__main__':
    tamper_block()
    

