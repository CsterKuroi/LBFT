from time import sleep
from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain

def get():
    # get tx by id
    b = Bigchain()
    tx_id = 'f457fd453607419aff5eb808b81e990fc8a21e99381627c52331a696aa9be34e'    
    tx = b.get_transaction(tx_id)
    return tx.to_dict()

if __name__=='__main__':
    print(get())
    
