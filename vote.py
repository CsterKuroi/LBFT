from bigchaindb.common.util import gen_timestamp, serialize
from bigchaindb.common import crypto
import create_keypairs as ck

def vote(decision,invalid_reason=None):
    vote = {
        'voting_for_block': '1',
        'previous_block': 'Genesis',
        'is_block_valid': decision,
        'invalid_reason': invalid_reason,
        'timestamp': gen_timestamp()
    }
    alice=ck.create()
    vote_data = serialize(vote)
    signature = crypto.PrivateKey(alice.signing_key).sign(vote_data.encode())

    vote_signed = {
        'node_pubkey': alice.verifying_key,
        'signature': signature.decode(),
        'vote': vote
    }

    return vote_signed

if __name__=="__main__":
    print(vote(True))
