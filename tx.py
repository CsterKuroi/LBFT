from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from bigchaindb.models import Transaction

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

def validate(ctx):
    tx_obj = Transaction.from_dict(ctx)
    input_conditions = []
    input_conditions.append(tx_obj.conditions[0])
#    print(tx_obj.fulfillments_valid(input_conditions))
    return(tx_obj.fulfillments_valid(input_conditions))

if __name__=="__main__":
    validate(create())
    
