from bigchaindb.common.transaction import Transaction, Asset
from bigchaindb.common.util import serialize

print(serialize(Asset().to_dict()))

print(serialize(Asset(data={"bicycle": {"manufacturer":  "bkfab" ,"serial_number":  "abcd1234"}}).to_dict()))
