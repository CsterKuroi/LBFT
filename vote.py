from bigchaindb.common.util import gen_timestamp, serialize
from bigchaindb.common import crypto
from bigchaindb_driver.crypto import generate_keypair
from itertools import compress
import math


def vote(decision,invalid_reason=None):
    vote = {
        'voting_for_block': '1',
        'previous_block': 'Genesis',
        'is_block_valid': decision,
        'invalid_reason': invalid_reason,
        'timestamp': gen_timestamp()
    }
    alice=generate_keypair()
    vote_data = serialize(vote)
    signature = crypto.PrivateKey(alice.signing_key).sign(vote_data.encode())

    vote_signed = {
        'node_pubkey': alice.verifying_key,
        'signature': signature.decode(),
        'vote': vote
    }

    return vote_signed

def verify(signed_vote):
    signature = signed_vote['signature']
    pk_base58 = signed_vote['node_pubkey']

    public_key = crypto.PublicKey(pk_base58)
    return public_key.verify(serialize(signed_vote['vote']).encode(), signature)

def election(voters,votes):
    n_voters = voters
    # vote_cast is the list of votes e.g. [True, True, False]
    vote_cast = [vote['vote']['is_block_valid'] for vote in votes]
    # vote_validity checks whether a vote is valid
    # or invalid, e.g. [False, True, True]
    vote_validity = [verify(vote) for vote in votes]

    # element-wise product of stated vote and validity of vote
    # vote_cast = [True, True, False] and
    # vote_validity = [False, True, True] gives
    # [True, False]
    # Only the correctly signed votes are tallied.
    vote_list = list(compress(vote_cast, vote_validity))

    # Total the votes. Here, valid and invalid refer
    # to the vote cast, not whether the vote itself
    # is valid or invalid.
    n_valid_votes = sum(vote_list)
    n_invalid_votes = len(vote_cast) - n_valid_votes

    if n_invalid_votes >= math.ceil(n_voters / 2):
        return ['INVALID',n_invalid_votes,n_voters]
    elif n_valid_votes > math.floor(n_voters / 2):
        return ['VALID',n_valid_votes,n_voters]
    else:
        return ['UNDECIDED',len(vote_cast),n_voters]

if __name__=="__main__":
    print(vote(True))
    print(verify(vote(True)))

