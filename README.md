# LBFT [Proof of Concept]

Layered BFT(Byzantine Fault Tolerant) Blockchain 

## Requires

1. `Python 3.5+`
2. `MPICH2`
3. `mpi4py`
4. `bigchaindb-driver`
5. `bigchaindb`

## QuickStart

```
mpirun -np 7 python3 core.py
```

## Topology
```
                                  +-------------+ 
                                  |     lv3     |
                                  |             |---o-
                                  |  rank = 6   | 
                                  +-------------+ 

                        +-------------+      +-------------+ 
                        |     lv2     |      |     lv3     |
                        |             |      |             |---o-
                        |  rank = 4   |      |  rank = 5   |
                        +-------------+      +-------------+

    +-------------+     +-------------+       +-------------+     +-------------+   
    |     lv1     |     |     lv1     |       |     lv1     |     |     lv1     |
    |             |     |             |       |             |     |             |---o-
    |  rank = 0   |     |  rank = 1   |       |  rank = 2   |     |  rank = 3   |
    +-------------+     +-------------+       +-------------+     +-------------+  
```
## Timeline

1. (↑)The lv1 nodes create `txs`, pass them to the lv2 nodes, and the lv2 nodes pass them to the lv3 node
2. (↓)The lv3 node creates a `block`, pass it to the lv2 nodes, and the lv2 nodes pass it to the lv1 nodes
3. (↑)The lv1 nodes validate the block then create `votes`, pass them to the lv2 nodes, and the lv2 nodes pass them to the lv3 node
4. (↓)The lv3 node collects all the votes as a `votelist`, pass it to the lv2 nodes, and the lv2 nodes pass it to the lv1 nodes .If more than 1/2 votes is valid, the node accepts the block.


## TaskList
- [x] topology

- [x] data_transmission

- [x] timeline

- [x] create_tx

- [x] tx_signature

- [x] validate_tx_signature

- [x] tx_list

- [ ] block_hash

- [ ] validate_block

- [ ] block_chain

- [ ] node_keypairs

- [x] vote

- [x] votes_list

- [x] vote_signature

- [x] verify_vote_signature

- [ ] scalability

- [ ] data_storage

- [ ] quota


## Files
### [`core.py`](./core.py)

1. Topology
2. data_transmission
3. timeline

### [`tx.py`](./tx.py)

1. Create tx
2. validate tx

### [`vote.py`](./vote.py)

1. Create vote
2. verify vote
3. checks if there are enough votes on that block to declare it valid or invalid

## Output
```
block: [
    {
        'transaction': {
            'asset': {
                'updatable': False,
                'id': '1879d4ca-19a5-428c-8f5e-7f8f0d11df49',
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                },
                'divisible': False,
                'refillable': False
            },
            'operation': 'CREATE',
            'metadata': {
                'id': '9e1a50e0-e02e-4221-8094-5172b402a631',
                'data': {
                    'planet': 'earth'
                }
            },
            'fulfillments': [
                {
                    'owners_before': [
                        '5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'
                    ],
                    'input': None,
                    'fulfillment': 'cf: 4: RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslOROyz3FLf64T9akgHcfAv6bNIeaBwiYqKXz7vJI7ar7CV8oQP25sp44TCzxZJBoomMBzNb1HQlL_zMhyHXnlGncN',
                    'fid': 0
                }
            ],
            'conditions': [
                {
                    'owners_after': [
                        '5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'
                    ],
                    'amount': 1,
                    'condition': {
                        'uri': 'cc: 4: 20: RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslORM: 96',
                        'details': {
                            'type_id': 4,
                            'type': 'fulfillment',
                            'signature': None,
                            'public_key': '5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz',
                            'bitmask': 32
                        }
                    },
                    'cid': 0
                }
            ]
        },
        'id': '96d39280816bc7652e577a87c04546ce7ee11d4576f1ae3c07a422ac3ca1f684',
        'version': 1
    },
    {
        'transaction': {
            'asset': {
                'updatable': False,
                'divisible': False,
                'id': '9560c113-3d61-48d6-b2d2-5d2d6bcc6c08',
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                },
                'refillable': False
            },
            'operation': 'CREATE',
            'metadata': {
                'id': '1963095e-6615-4433-a434-e6504cdf8137',
                'data': {
                    'planet': 'earth'
                }
            },
            'fulfillments': [
                {
                    'owners_before': [
                        '2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'
                    ],
                    'input': None,
                    'fulfillment': 'cf: 4: FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeBtM7rHUTaxuEqZJE-ehxb-wMlEqhsvyHXEu7-745LPEfwDufuTqBOUThP4lhPXTUI8pXVWHnzq0DUFZTIgDNcC',
                    'fid': 0
                }
            ],
            'conditions': [
                {
                    'owners_after': [
                        '2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'
                    ],
                    'amount': 1,
                    'condition': {
                        'uri': 'cc: 4: 20: FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeA: 96',
                        'details': {
                            'type_id': 4,
                            'type': 'fulfillment',
                            'signature': None,
                            'public_key': '2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR',
                            'bitmask': 32
                        }
                    },
                    'cid': 0
                }
            ]
        },
        'id': '9aaec84aa0ce373793e132d7ab4d4df7cca60150deb6bca695888091c74c7f1b',
        'version': 1
    },
    {
        'transaction': {
            'asset': {
                'updatable': False,
                'divisible': False,
                'id': '4bf8d2d2-fc8e-43b8-b851-3b3a5a8e1722',
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                },
                'refillable': False
            },
            'operation': 'CREATE',
            'metadata': {
                'id': '01184ca5-9680-402e-ad89-c95145b2c6cb',
                'data': {
                    'planet': 'earth'
                }
            },
            'fulfillments': [
                {
                    'owners_before': [
                        '88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'
                    ],
                    'input': None,
                    'fulfillment': 'cf: 4: aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOR3YG0yWKNM4u7mFpOx1edsveEukMvN7FJeOKfr-H6YVlxpZU-qV5GxxOC7S0gaTw5U7F0my8BYvSoZxB_qt6wH',
                    'fid': 0
                }
            ],
            'conditions': [
                {
                    'owners_after': [
                        '88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'
                    ],
                    'amount': 1,
                    'condition': {
                        'uri': 'cc: 4: 20: aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOQ: 96',
                        'details': {
                            'type_id': 4,
                            'type': 'fulfillment',
                            'signature': None,
                            'public_key': '88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P',
                            'bitmask': 32
                        }
                    },
                    'cid': 0
                }
            ]
        },
        'id': '4d36c0ac00f6c29c57c62ae80c9ff30695c0b49eaa4066ad7ffd8ae831f9647a',
        'version': 1
    },
    {
        'transaction': {
            'asset': {
                'updatable': False,
                'id': '13f952aa-164f-479a-8de7-5c5615be9cf2',
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                },
                'divisible': False,
                'refillable': False
            },
            'operation': 'CREATE',
            'metadata': {
                'id': '40979cee-4096-4157-8645-62bb07dfbab1',
                'data': {
                    'planet': 'earth'
                }
            },
            'fulfillments': [
                {
                    'owners_before': [
                        '7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'
                    ],
                    'input': None,
                    'fulfillment': 'cf: 4: ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s0BHa4L0U4k7PiLXiI_aIxwi2kdj6kTKvxN-psMoe0kl8ZL60uGb_MIJUp3FKhFuIf5gBbz9sCDnUqVOGmm2IE',
                    'fid': 0
                }
            ],
            'conditions': [
                {
                    'owners_after': [
                        '7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'
                    ],
                    'amount': 1,
                    'condition': {
                        'uri': 'cc: 4: 20: ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s: 96',
                        'details': {
                            'type_id': 4,
                            'type': 'fulfillment',
                            'signature': None,
                            'public_key': '7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx',
                            'bitmask': 32
                        }
                    },
                    'cid': 0
                }
            ]
        },
        'id': 'b99858376a7a1d6283aaa55dab9b448a9b349f889be5053aa3c8a37d6425b57a',
        'version': 1
    }
]
```

```
votes: [
    {
        'signature': '4AJ7qUU6CkAxW2ipTPBviuaVn9e7waKE4hah56u4cbwVmcEhH6miYSqZfrG7JnHQQj8zoNk7QnjDkW7gfe9BmfC',
        'vote': {
            'invalid_reason': None,
            'voting_for_block': '1',
            'previous_block': 'Genesis',
            'is_block_valid': True,
            'timestamp': '1482410513'
        },
        'node_pubkey': 'FxhfnvpiZbyYPLFz1cD8kdbeNVmHmM8tFcqCrFzLuri'
    },
    {
        'vote': {
            'invalid_reason': None,
            'voting_for_block': '1',
            'is_block_valid': True,
            'previous_block': 'Genesis',
            'timestamp': '1482410513'
        },
        'signature': '3ujTJXzYvKBWMDTQgiDBdyNPcxhF2Mr5oTYMJVUAoFJAUZXi7qhVsfQ6q6brdHMy3ykWBbq5mJo8ToXCHYS2ra6h',
        'node_pubkey': 'HcNPQ25G2qsSytbegM3fbEscPyXhvG64cDVXhzRTXsMF'
    },
    {
        'signature': '2HzioaYPVgKcsYF9BYHZhtXU2Wm6Xm5fyneybrapsHQF9597GKzLNkzYHTm6CTMzwaa3yrCrRgeFbx7LCsfMiZ6',
        'vote': {
            'invalid_reason': None,
            'voting_for_block': '1',
            'is_block_valid': True,
            'previous_block': 'Genesis',
            'timestamp': '1482410513'
        },
        'node_pubkey': '3GfvMY1JY6T3nDzevPmXViE1MtXd7JpGDXamvTKTZTom'
    },
    {
        'signature': '8rC3q1Ac5hsQsBZpKNUN6rxh9BtZenfeUWDv8xgYZtVZ8S8udm7SGK8XfLbetm5VAfqC5Y34ahktzhumKccUr77',
        'vote': {
            'invalid_reason': None,
            'voting_for_block': '1',
            'previous_block': 'Genesis',
            'is_block_valid': True,
            'timestamp': '1482410513'
        },
        'node_pubkey': '3AVtrmkNi3nUzqueec7kGgr8Am11AbCxQStAyCc3kjWw'
    },
    {
        'signature': '33rzqqtymgwj6VD3p5d3M8mFC9LjVcX47D3duJE3Jkhkg72TZaCrgYtWq5fVemNrr2R9TD65RmuhVPMQYBTBMp2o',
        'vote': {
            'invalid_reason': None,
            'voting_for_block': '1',
            'is_block_valid': True,
            'previous_block': 'Genesis',
            'timestamp': '1482410513'
        },
        'node_pubkey': '5UMMbgr4YhJbjXYtu8AkZFXSvJwHM6qLXJYMS2Cn9Ftw'
    },
    {
        'signature': '2Spg7LQ9VHQbBwwLJYXuhPaegEJZ7dFznsfivEyQZhPr3NH9C9wHjpgtfMuLEENZPM1mUdQsuSZ9AXaRcmnvimGT',
        'vote': {
            'invalid_reason': None,
            'voting_for_block': '1',
            'is_block_valid': True,
            'previous_block': 'Genesis',
            'timestamp': '1482410513'
        },
        'node_pubkey': 'Ao1gzjqs9T5JGWqoh2MH6SmykV2coFJsKCAofP7dyMvY'
    },
    {
        'signature': '28JuaMyUdrM13Zo6sEQpogdjpC7ZCJh35DrptU3evEkfFeYHyBL14txMCHRUCvNiMn8y4TrXpW6Y5aGADvf91LgB',
        'vote': {
            'invalid_reason': None,
            'voting_for_block': '1',
            'is_block_valid': True,
            'previous_block': 'Genesis',
            'timestamp': '1482410513'
        },
        'node_pubkey': 'HZaVUaq8aFs3WT9vbnGgoSXfAKgbJ1G5uSHzPTtvhSBM'
    }
]
```

```
rank 6: ['VALID', 7, 7]
rank 5: ['VALID', 7, 7]
rank 2: ['VALID', 7, 7]
rank 2 time:0.366696s

rank 4: ['VALID', 7, 7]
rank 0: ['VALID', 7, 7]
rank 0 time:0.440076s

rank 3: ['VALID', 7, 7]
rank 3 time:0.322589s

rank 1: ['VALID', 7, 7]
rank 1 time:0.295617s
```

## Links
* [bigchaindb](https://github.com/bigchaindb/bigchaindb)
* [mpi4py](https://github.com/mpi4py/mpi4py)
