from time import sleep
from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain

def get():
    # get tx by id
    b = Bigchain()
    tx_id = 'd42ea9c8e926f91f1f922e30a1c84e1a92f100e935c4b0e42338719e42e494dd'    
    tx = b.get_transaction(tx_id)
    return tx.to_dict()

if __name__=='__main__':
    print(get())
    
