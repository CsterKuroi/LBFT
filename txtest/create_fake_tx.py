from time import sleep
from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset, Fulfillment
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain

def create_transfer():
    ##################################################### 1.CREATE
    # Cryptographic Identities Generation
    alice, bob = generate_keypair(), generate_keypair()
    
    # Digital Asset Definition (e.g. bicycle)
    asset = Asset(data={"bicycle": {"manufacturer":  "bkfab" ,"serial_number":  "abcd1234"}})

    # Metadata Definition
    metadata = {'planet': 'earth'}

    # create trnsaction  TODO : owners_before might be node_pubkey in v0.8.0
    tx = Transaction.create([alice.public_key], [alice.public_key], metadata = metadata, asset = asset)
    print(" ")
    print("1.tx_create asset id    :  alice-----bicycle(",tx.to_dict()['transaction']['asset']['id'],")----->alice")
    print("1.tx_create tx id       : ",tx.to_dict()['id'])

    # sign with alice's private key
    tx = tx.sign([alice.private_key])
    tx_id = tx.to_dict()['id']

    # write to backlog
    b = Bigchain()
    print("1.tx_create db response : ",b.write_transaction(tx))

    # wait 2 sec
    sleep(2)

    # get tx by id
    tx = b.get_transaction(tx_id)
    print("1.tx_create query       : ",tx)
    # print("tx1_id:"+tx.to_dict()['id'])
    print(" ")
    ##################################################### 2.TRANSFER
    #  inputs and asset [fake]
    cid = 0
    condition = tx.to_dict()['transaction']['conditions'][cid]
    inputs =Fulfillment.from_dict({
        'fulfillment': condition['condition']['details'],
        'input': {
            'cid': cid,
            'txid': tx.to_dict()['id'],
         },
         'owners_before': [bob.public_key],
    })
    asset = Asset.from_dict(tx.to_dict()['transaction']['asset'])

    # transfer
    tx = Transaction.transfer([inputs], [bob.public_key],asset)
    print("2.tx_fake asset id    :  bob-----bicycle(",tx.to_dict()['transaction']['asset']['id'],")----->bob")
    print("2.tx_fake tx id       : ",tx.to_dict()['id'])

    # sign with bob's private key [fake]
    tx = tx.sign([bob.private_key])
    tx_id = tx.to_dict()['id']

    # write to backlog
    b = Bigchain()
    print("2.tx_fake db response : ",b.write_transaction(tx))

    # wait 2 sec
    sleep(2)

    # get tx by id
    tx = b.get_transaction(tx_id)
    print("2.tx_fake query       : ",tx)
    #print("tx2_id:"+tx.to_dict()['id'])
    print(" ")
if __name__=='__main__':
    create_transfer()
    
