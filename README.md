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

- [x] validate tx_signature

- [x] create_block

- [ ] block_chain

- [ ] validate_block

- [ ] node_keypairs

- [x] vote

- [x] votes_list

- [ ] vote_signature

- [ ] validate vote_signature

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

rank 3 :Get block [{'transaction': {'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'id': '1879d4ca-19a5-428c-8f5e-7f8f0d11df49'}, 'metadata': {'data': {'planet': 'earth'}, 'id': '9e1a50e0-e02e-4221-8094-5172b402a631'}, 'conditions': [{'cid': 0, 'condition': {'uri': 'cc:4:20:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslORM:96', 'details': {'public_key': '5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz', 'type_id': 4, 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'owners_after': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'], 'amount': 1}], 'fulfillments': [{'fid': 0, 'owners_before': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'], 'input': None, 'fulfillment': 'cf:4:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslOROyz3FLf64T9akgHcfAv6bNIeaBwiYqKXz7vJI7ar7CV8oQP25sp44TCzxZJBoomMBzNb1HQlL_zMhyHXnlGncN'}], 'operation': 'CREATE'}, 'id': '96d39280816bc7652e577a87c04546ce7ee11d4576f1ae3c07a422ac3ca1f684', 'version': 1}, {'transaction': {'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'id': '9560c113-3d61-48d6-b2d2-5d2d6bcc6c08'}, 'metadata': {'data': {'planet': 'earth'}, 'id': '1963095e-6615-4433-a434-e6504cdf8137'}, 'conditions': [{'cid': 0, 'condition': {'uri': 'cc:4:20:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeA:96', 'details': {'public_key': '2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR', 'type_id': 4, 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'owners_after': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'], 'amount': 1}], 'fulfillments': [{'fid': 0, 'owners_before': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'], 'input': None, 'fulfillment': 'cf:4:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeBtM7rHUTaxuEqZJE-ehxb-wMlEqhsvyHXEu7-745LPEfwDufuTqBOUThP4lhPXTUI8pXVWHnzq0DUFZTIgDNcC'}], 'operation': 'CREATE'}, 'id': '9aaec84aa0ce373793e132d7ab4d4df7cca60150deb6bca695888091c74c7f1b', 'version': 1}, {'transaction': {'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'id': '4bf8d2d2-fc8e-43b8-b851-3b3a5a8e1722'}, 'metadata': {'data': {'planet': 'earth'}, 'id': '01184ca5-9680-402e-ad89-c95145b2c6cb'}, 'conditions': [{'cid': 0, 'condition': {'uri': 'cc:4:20:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOQ:96', 'details': {'public_key': '88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P', 'type_id': 4, 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'owners_after': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'], 'amount': 1}], 'fulfillments': [{'fid': 0, 'owners_before': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'], 'input': None, 'fulfillment': 'cf:4:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOR3YG0yWKNM4u7mFpOx1edsveEukMvN7FJeOKfr-H6YVlxpZU-qV5GxxOC7S0gaTw5U7F0my8BYvSoZxB_qt6wH'}], 'operation': 'CREATE'}, 'id': '4d36c0ac00f6c29c57c62ae80c9ff30695c0b49eaa4066ad7ffd8ae831f9647a', 'version': 1}, {'transaction': {'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'id': '13f952aa-164f-479a-8de7-5c5615be9cf2'}, 'metadata': {'data': {'planet': 'earth'}, 'id': '40979cee-4096-4157-8645-62bb07dfbab1'}, 'conditions': [{'cid': 0, 'condition': {'uri': 'cc:4:20:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s:96', 'details': {'public_key': '7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx', 'type_id': 4, 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'owners_after': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'], 'amount': 1}], 'fulfillments': [{'fid': 0, 'owners_before': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'], 'input': None, 'fulfillment': 'cf:4:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s0BHa4L0U4k7PiLXiI_aIxwi2kdj6kTKvxN-psMoe0kl8ZL60uGb_MIJUp3FKhFuIf5gBbz9sCDnUqVOGmm2IE'}], 'operation': 'CREATE'}, 'id': 'b99858376a7a1d6283aaa55dab9b448a9b349f889be5053aa3c8a37d6425b57a', 'version': 1}]
rank 3 :Get votes {0, 2, 4, 6, 8, 10, 12}
rank 3 time:0.128054s

rank 0 :Get block [{'transaction': {'asset': {'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'divisible': False, 'refillable': False, 'updatable': False, 'id': '1879d4ca-19a5-428c-8f5e-7f8f0d11df49'}, 'conditions': [{'owners_after': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'], 'amount': 1, 'condition': {'details': {'type_id': 4, 'signature': None, 'public_key': '5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz', 'type': 'fulfillment', 'bitmask': 32}, 'uri': 'cc:4:20:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslORM:96'}, 'cid': 0}], 'metadata': {'data': {'planet': 'earth'}, 'id': '9e1a50e0-e02e-4221-8094-5172b402a631'}, 'fulfillments': [{'fulfillment': 'cf:4:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslOROyz3FLf64T9akgHcfAv6bNIeaBwiYqKXz7vJI7ar7CV8oQP25sp44TCzxZJBoomMBzNb1HQlL_zMhyHXnlGncN', 'input': None, 'owners_before': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'], 'fid': 0}], 'operation': 'CREATE'}, 'version': 1, 'id': '96d39280816bc7652e577a87c04546ce7ee11d4576f1ae3c07a422ac3ca1f684'}, {'transaction': {'asset': {'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'divisible': False, 'refillable': False, 'updatable': False, 'id': '9560c113-3d61-48d6-b2d2-5d2d6bcc6c08'}, 'conditions': [{'owners_after': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'], 'amount': 1, 'condition': {'details': {'type_id': 4, 'signature': None, 'public_key': '2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR', 'type': 'fulfillment', 'bitmask': 32}, 'uri': 'cc:4:20:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeA:96'}, 'cid': 0}], 'metadata': {'data': {'planet': 'earth'}, 'id': '1963095e-6615-4433-a434-e6504cdf8137'}, 'fulfillments': [{'fulfillment': 'cf:4:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeBtM7rHUTaxuEqZJE-ehxb-wMlEqhsvyHXEu7-745LPEfwDufuTqBOUThP4lhPXTUI8pXVWHnzq0DUFZTIgDNcC', 'input': None, 'owners_before': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'], 'fid': 0}], 'operation': 'CREATE'}, 'version': 1, 'id': '9aaec84aa0ce373793e132d7ab4d4df7cca60150deb6bca695888091c74c7f1b'}, {'transaction': {'asset': {'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'divisible': False, 'refillable': False, 'updatable': False, 'id': '4bf8d2d2-fc8e-43b8-b851-3b3a5a8e1722'}, 'conditions': [{'owners_after': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'], 'amount': 1, 'condition': {'details': {'type_id': 4, 'signature': None, 'public_key': '88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P', 'type': 'fulfillment', 'bitmask': 32}, 'uri': 'cc:4:20:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOQ:96'}, 'cid': 0}], 'metadata': {'data': {'planet': 'earth'}, 'id': '01184ca5-9680-402e-ad89-c95145b2c6cb'}, 'fulfillments': [{'fulfillment': 'cf:4:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOR3YG0yWKNM4u7mFpOx1edsveEukMvN7FJeOKfr-H6YVlxpZU-qV5GxxOC7S0gaTw5U7F0my8BYvSoZxB_qt6wH', 'input': None, 'owners_before': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'], 'fid': 0}], 'operation': 'CREATE'}, 'version': 1, 'id': '4d36c0ac00f6c29c57c62ae80c9ff30695c0b49eaa4066ad7ffd8ae831f9647a'}, {'transaction': {'asset': {'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'divisible': False, 'refillable': False, 'updatable': False, 'id': '13f952aa-164f-479a-8de7-5c5615be9cf2'}, 'conditions': [{'owners_after': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'], 'amount': 1, 'condition': {'details': {'type_id': 4, 'signature': None, 'public_key': '7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx', 'type': 'fulfillment', 'bitmask': 32}, 'uri': 'cc:4:20:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s:96'}, 'cid': 0}], 'metadata': {'data': {'planet': 'earth'}, 'id': '40979cee-4096-4157-8645-62bb07dfbab1'}, 'fulfillments': [{'fulfillment': 'cf:4:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s0BHa4L0U4k7PiLXiI_aIxwi2kdj6kTKvxN-psMoe0kl8ZL60uGb_MIJUp3FKhFuIf5gBbz9sCDnUqVOGmm2IE', 'input': None, 'owners_before': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'], 'fid': 0}], 'operation': 'CREATE'}, 'version': 1, 'id': 'b99858376a7a1d6283aaa55dab9b448a9b349f889be5053aa3c8a37d6425b57a'}]
rank 0 :Get votes {0, 2, 4, 6, 8, 10, 12}
rank 0 time:0.148640s

rank 2 :Get block [{'version': 1, 'transaction': {'fulfillments': [{'input': None, 'owners_before': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'], 'fulfillment': 'cf:4:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslOROyz3FLf64T9akgHcfAv6bNIeaBwiYqKXz7vJI7ar7CV8oQP25sp44TCzxZJBoomMBzNb1HQlL_zMhyHXnlGncN', 'fid': 0}], 'operation': 'CREATE', 'conditions': [{'owners_after': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'], 'cid': 0, 'condition': {'details': {'signature': None, 'bitmask': 32, 'type_id': 4, 'type': 'fulfillment', 'public_key': '5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'}, 'uri': 'cc:4:20:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslORM:96'}, 'amount': 1}], 'asset': {'updatable': False, 'id': '1879d4ca-19a5-428c-8f5e-7f8f0d11df49', 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'divisible': False}, 'metadata': {'id': '9e1a50e0-e02e-4221-8094-5172b402a631', 'data': {'planet': 'earth'}}}, 'id': '96d39280816bc7652e577a87c04546ce7ee11d4576f1ae3c07a422ac3ca1f684'}, {'version': 1, 'transaction': {'fulfillments': [{'input': None, 'owners_before': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'], 'fulfillment': 'cf:4:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeBtM7rHUTaxuEqZJE-ehxb-wMlEqhsvyHXEu7-745LPEfwDufuTqBOUThP4lhPXTUI8pXVWHnzq0DUFZTIgDNcC', 'fid': 0}], 'operation': 'CREATE', 'conditions': [{'owners_after': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'], 'cid': 0, 'condition': {'details': {'signature': None, 'bitmask': 32, 'type_id': 4, 'type': 'fulfillment', 'public_key': '2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'}, 'uri': 'cc:4:20:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeA:96'}, 'amount': 1}], 'asset': {'updatable': False, 'id': '9560c113-3d61-48d6-b2d2-5d2d6bcc6c08', 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'divisible': False}, 'metadata': {'id': '1963095e-6615-4433-a434-e6504cdf8137', 'data': {'planet': 'earth'}}}, 'id': '9aaec84aa0ce373793e132d7ab4d4df7cca60150deb6bca695888091c74c7f1b'}, {'version': 1, 'transaction': {'fulfillments': [{'input': None, 'owners_before': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'], 'fulfillment': 'cf:4:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOR3YG0yWKNM4u7mFpOx1edsveEukMvN7FJeOKfr-H6YVlxpZU-qV5GxxOC7S0gaTw5U7F0my8BYvSoZxB_qt6wH', 'fid': 0}], 'operation': 'CREATE', 'conditions': [{'owners_after': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'], 'cid': 0, 'condition': {'details': {'signature': None, 'bitmask': 32, 'type_id': 4, 'type': 'fulfillment', 'public_key': '88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'}, 'uri': 'cc:4:20:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOQ:96'}, 'amount': 1}], 'asset': {'updatable': False, 'id': '4bf8d2d2-fc8e-43b8-b851-3b3a5a8e1722', 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'divisible': False}, 'metadata': {'id': '01184ca5-9680-402e-ad89-c95145b2c6cb', 'data': {'planet': 'earth'}}}, 'id': '4d36c0ac00f6c29c57c62ae80c9ff30695c0b49eaa4066ad7ffd8ae831f9647a'}, {'version': 1, 'transaction': {'fulfillments': [{'input': None, 'owners_before': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'], 'fulfillment': 'cf:4:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s0BHa4L0U4k7PiLXiI_aIxwi2kdj6kTKvxN-psMoe0kl8ZL60uGb_MIJUp3FKhFuIf5gBbz9sCDnUqVOGmm2IE', 'fid': 0}], 'operation': 'CREATE', 'conditions': [{'owners_after': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'], 'cid': 0, 'condition': {'details': {'signature': None, 'bitmask': 32, 'type_id': 4, 'type': 'fulfillment', 'public_key': '7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'}, 'uri': 'cc:4:20:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s:96'}, 'amount': 1}], 'asset': {'updatable': False, 'id': '13f952aa-164f-479a-8de7-5c5615be9cf2', 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'refillable': False, 'divisible': False}, 'metadata': {'id': '40979cee-4096-4157-8645-62bb07dfbab1', 'data': {'planet': 'earth'}}}, 'id': 'b99858376a7a1d6283aaa55dab9b448a9b349f889be5053aa3c8a37d6425b57a'}]
rank 2 :Get votes {0, 2, 4, 6, 8, 10, 12}
rank 2 time:0.137464s

rank 1 :Get block [{'id': '96d39280816bc7652e577a87c04546ce7ee11d4576f1ae3c07a422ac3ca1f684', 'version': 1, 'transaction': {'metadata': {'id': '9e1a50e0-e02e-4221-8094-5172b402a631', 'data': {'planet': 'earth'}}, 'operation': 'CREATE', 'conditions': [{'owners_after': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz'], 'amount': 1, 'condition': {'uri': 'cc:4:20:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslORM:96', 'details': {'type_id': 4, 'public_key': '5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz', 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'cid': 0}], 'asset': {'id': '1879d4ca-19a5-428c-8f5e-7f8f0d11df49', 'refillable': False, 'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}}, 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:RdzOBlnP-eg1wibIklfJ-CgEsm66LlHz0YgyqaslOROyz3FLf64T9akgHcfAv6bNIeaBwiYqKXz7vJI7ar7CV8oQP25sp44TCzxZJBoomMBzNb1HQlL_zMhyHXnlGncN', 'fid': 0, 'owners_before': ['5hiQu2Jf9bXHhbXreLcYxPC1GyH4L97npm9rvwjXDccz']}]}}, {'id': '9aaec84aa0ce373793e132d7ab4d4df7cca60150deb6bca695888091c74c7f1b', 'version': 1, 'transaction': {'metadata': {'id': '1963095e-6615-4433-a434-e6504cdf8137', 'data': {'planet': 'earth'}}, 'operation': 'CREATE', 'conditions': [{'owners_after': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR'], 'amount': 1, 'condition': {'uri': 'cc:4:20:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeA:96', 'details': {'type_id': 4, 'public_key': '2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR', 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'cid': 0}], 'asset': {'id': '9560c113-3d61-48d6-b2d2-5d2d6bcc6c08', 'refillable': False, 'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}}, 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:FJXkCJ1SoovqFtveHpEMHz_2pIv8waWU4F4lbyqdGeBtM7rHUTaxuEqZJE-ehxb-wMlEqhsvyHXEu7-745LPEfwDufuTqBOUThP4lhPXTUI8pXVWHnzq0DUFZTIgDNcC', 'fid': 0, 'owners_before': ['2PMiegwgoqAfzxFs5wVJ6yiotSz2BggEjjKifjHpT5DR']}]}}, {'id': '4d36c0ac00f6c29c57c62ae80c9ff30695c0b49eaa4066ad7ffd8ae831f9647a', 'version': 1, 'transaction': {'metadata': {'id': '01184ca5-9680-402e-ad89-c95145b2c6cb', 'data': {'planet': 'earth'}}, 'operation': 'CREATE', 'conditions': [{'owners_after': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P'], 'amount': 1, 'condition': {'uri': 'cc:4:20:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOQ:96', 'details': {'type_id': 4, 'public_key': '88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P', 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'cid': 0}], 'asset': {'id': '4bf8d2d2-fc8e-43b8-b851-3b3a5a8e1722', 'refillable': False, 'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}}, 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:aeIjLq1BFq7sLgg1CHSmZuuwxlol6DM1d4zblI_pUOR3YG0yWKNM4u7mFpOx1edsveEukMvN7FJeOKfr-H6YVlxpZU-qV5GxxOC7S0gaTw5U7F0my8BYvSoZxB_qt6wH', 'fid': 0, 'owners_before': ['88KoiDUfJgjDbty6fGFpCfGzTPhCfYDVNLv9mJkF898P']}]}}, {'id': 'b99858376a7a1d6283aaa55dab9b448a9b349f889be5053aa3c8a37d6425b57a', 'version': 1, 'transaction': {'metadata': {'id': '40979cee-4096-4157-8645-62bb07dfbab1', 'data': {'planet': 'earth'}}, 'operation': 'CREATE', 'conditions': [{'owners_after': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx'], 'amount': 1, 'condition': {'uri': 'cc:4:20:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s:96', 'details': {'type_id': 4, 'public_key': '7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx', 'type': 'fulfillment', 'signature': None, 'bitmask': 32}}, 'cid': 0}], 'asset': {'id': '13f952aa-164f-479a-8de7-5c5615be9cf2', 'refillable': False, 'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}}, 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:ZXHTzUaw6YrcfBVvo9SaAmFNeedW9kewRdqIeLuye8s0BHa4L0U4k7PiLXiI_aIxwi2kdj6kTKvxN-psMoe0kl8ZL60uGb_MIJUp3FKhFuIf5gBbz9sCDnUqVOGmm2IE', 'fid': 0, 'owners_before': ['7pzr8B6EyHQzTtbLZjq4QSAdbaNbj23qqnJcTZCSq7Xx']}]}}]
rank 1 :Get votes {0, 2, 4, 6, 8, 10, 12}
rank 1 time:0.155984s
```
