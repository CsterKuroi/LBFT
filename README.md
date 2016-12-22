# LBFT

Layered BFT(Byzantine Fault Tolerant) Blockchain 

[Proof of Concept]

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


## Task List
- [x] topology

- [x] Timeline

- [x] data_transmission

- [x] create_tx

- [x] tx_signature

- [x] validate_tx_signature

- [x] create_block

- [ ] block_chain

- [ ] validate_block

- [ ] node_keypairs

- [x] vote

- [x] votes_list

- [ ] vote_signature

- [ ] verify_vote_signature

- [ ] scalability

- [ ] data_storage

- [ ] quota

## Quick Start
requires = [
   'Python 3.5+'
   'MPICH2',
   'mpi4py',
   'bigchaindb-driver',
   'bigchaindb',
]


```
mpirun -np 7 python3 tx124.py
```

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
        'vote': {
            'timestamp': '1482408347',
            'is_block_valid': True,
            'invalid_reason': None,
            'previous_block': 'Genesis',
            'voting_for_block': '1'
        },
        'node_pubkey': 'C8A4Q7WqcPzRBhP6THMERGXHZpECyb4NpjdfCGH8g7hq',
        'signature': '5mShzaP3PHMNwJ6LirU8yYQiRCc6sBr1noFoKdHiNFxghvuwZYeGyYzx4puGTASYHBgBPzbwBRjwQXqoCkCPYpgy'
    },
    {
        'vote': {
            'timestamp': '1482408347',
            'is_block_valid': True,
            'invalid_reason': None,
            'previous_block': 'Genesis',
            'voting_for_block': '1'
        },
        'node_pubkey': '8zZM6s6fmzsBYaEFYgqwRAotYJjcEyL4dyPo3bXTQpt1',
        'signature': '1216Ea1xeJnNdcbfcykxjEuRrtvVwFwoCabRyF9Gj6xdNxBU6maArnCKWz4cm5kU4ZTVJwP9WtbNTFAWQU8yK3pi'
    },
    {
        'vote': {
            'timestamp': '1482408347',
            'previous_block': 'Genesis',
            'invalid_reason': None,
            'is_block_valid': True,
            'voting_for_block': '1'
        },
        'node_pubkey': 'FoR36wY9W4zgFL69LhwfSmgtVyvG21MQNdYP4YgWyggK',
        'signature': '47DP4nbJ48ixWyto3vvwc5tQDBx4rAEMeZfTUGvnAqWaGMuQ6x8nErQK7ApVpuknScoDiPxYeCRBVyRKDAuG551p'
    },
    {
        'vote': {
            'timestamp': '1482408347',
            'is_block_valid': True,
            'invalid_reason': None,
            'previous_block': 'Genesis',
            'voting_for_block': '1'
        },
        'node_pubkey': 'EZWddJACrgYoz1LaeRref3hsjhFgcybPqVoVwX2bHbi9',
        'signature': 'Xq9EG5ShEwxWBFp8DLA9KkP8AwUphVbTatXagtuq6sydetxWPQGFKvyDqxgSHdPxqeSLFfzBNFSqjSfE78mgJVR'
    },
    {
        'vote': {
            'timestamp': '1482408347',
            'previous_block': 'Genesis',
            'invalid_reason': None,
            'is_block_valid': True,
            'voting_for_block': '1'
        },
        'node_pubkey': '51DdsFjDBysVMtSYsUfsgwHMVp78ZCCLd2xFBn7K2KoU',
        'signature': '46rs5AFiypCwjFtYbmVwbTZVHsZuwaoeFBkvZAjSV6ntNGTTD8XWEf8hToDy7ZyKnYmgCwcQHSAaHZQgQ3pr5P9J'
    }
]
```

```
rank 3 time:0.111959s

rank 0 time:0.148191s

rank 2 time:0.135983s

rank 1 time:0.144461s
```
