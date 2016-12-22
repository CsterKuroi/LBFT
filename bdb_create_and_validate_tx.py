import tx
from bigchaindb.models import Transaction

ctx=tx.create()
print(ctx)
tx_obj = Transaction.from_dict(ctx)
input_conditions = []
input_conditions.append(tx_obj.conditions[0])
print(tx_obj.fulfillments_valid(input_conditions))

