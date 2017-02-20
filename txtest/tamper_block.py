from time import sleep
from crypto import generate_keypair,hash_data
from bigchaindb.common.transaction import Transaction, Asset
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain
from bigchaindb.models import Block

def tamper_block():
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
    tx_id = tx.to_dict()['id']
    print("tx_id                       : ",tx_id)

    # create block 
    b = Bigchain()
    block = b.create_block([tx])
    print("block timestamp right now   : ",block.to_dict()['block']['timestamp'])
    # tamper block
    block.timestamp = '1'
    print("tamper block.timestamp to 1 : ")
    block_id = block.to_dict()['id']
    block_voters = block.to_dict()['block']['voters']
    
    print("block timestamp right now   : ",block.to_dict()['block']['timestamp'])
    print("tamper_block_id             : ",block_id)
    print("db response                 : ",b.write_block(block))
    sleep(2)
    print("tamper_block status         : ",b.block_election_status(block_id,block_voters))
    print("blocks_status_containing_tx : ",b.get_blocks_status_containing_tx(tx_id))
    print(" ")

if __name__=='__main__':
    tamper_block()
    

