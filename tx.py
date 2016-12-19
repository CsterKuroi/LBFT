from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

def create():
    bdb = BigchainDB('http://localhost:9984/api/v1')
    bicycle = {
     'data': {
         'bicycle': {
             'serial_number': 'abcd1234',
             'manufacturer': 'bkfab',
         },
     },
    }
    metadata = {'planet': 'earth'}
    alice, bob = generate_keypair(), generate_keypair()
    prepared_creation_tx = bdb.transactions.prepare(
         operation='CREATE',
         owners_before=alice.verifying_key,
         asset=bicycle,
         metadata=metadata,
    )
    fulfilled_creation_tx = bdb.transactions.fulfill(
         prepared_creation_tx, private_keys=alice.signing_key)
#    print(fulfilled_creation_tx)
#    txid = fulfilled_creation_tx['id']
#    print(txid)
    return(fulfilled_creation_tx)

if __name__=="__main__":
    create()

