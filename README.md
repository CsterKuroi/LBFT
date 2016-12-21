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
        'version': 1,
        'transaction': {
            'asset': {
                'updatable': False,
                'id': '5f811a71-a02e-45fd-82b2-e29264cc6c37',
                'divisible': False,
                'refillable': False,
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                }
            },
            'conditions': [
                {
                    'owners_after': [
                        '3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs'
                    ],
                    'cid': 0,
                    'condition': {
                        'uri': 'cc: 4: 20: JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKo: 96',
                        'details': {
                            'public_key': '3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs',
                            'signature': None,
                            'type': 'fulfillment',
                            'bitmask': 32,
                            'type_id': 4
                        }
                    },
                    'amount': 1
                }
            ],
            'metadata': {
                'data': {
                    'planet': 'earth'
                },
                'id': '372f2c14-fbbd-4cb5-90db-6713610f45e2'
            },
            'fulfillments': [
                {
                    'input': None,
                    'owners_before': [
                        '3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs'
                    ],
                    'fulfillment': 'cf: 4: JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKodWMC0w9kkRFIvmw9AOSvTGdu4YR6KOYN_Y8oWsEinumNNpf8YD8mYPTn0zjzjA4iVnyh_9EKckbmOkED88YcF',
                    'fid': 0
                }
            ],
            'operation': 'CREATE'
        },
        'id': '7858420600dc8adc991491e49d93006d38b9cdc655f62eacaa1a6b745e438231'
    },
    {
        'version': 1,
        'transaction': {
            'asset': {
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                },
                'updatable': False,
                'divisible': False,
                'id': '5108d68e-3386-487d-a5ca-bfcf068a7727',
                'refillable': False
            },
            'conditions': [
                {
                    'owners_after': [
                        'C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw'
                    ],
                    'cid': 0,
                    'condition': {
                        'uri': 'cc: 4: 20: pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04: 96',
                        'details': {
                            'type_id': 4,
                            'public_key': 'C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw',
                            'signature': None,
                            'bitmask': 32,
                            'type': 'fulfillment'
                        }
                    },
                    'amount': 1
                }
            ],
            'metadata': {
                'data': {
                    'planet': 'earth'
                },
                'id': '5d072559-51c0-45e1-bf2f-a4b604b3cffb'
            },
            'fulfillments': [
                {
                    'input': None,
                    'owners_before': [
                        'C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw'
                    ],
                    'fulfillment': 'cf: 4: pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04_NngxF-Z9e4s8F78cLr7MZ4TVmO7ezS_WtZFJ2-3TjQWEHL_q36kB0BGW1KR6u3A8CUthRyTWEbFKjeoW9Q8I',
                    'fid': 0
                }
            ],
            'operation': 'CREATE'
        },
        'id': '62f607164b394c540219996152e56235eee328add973d1d7ba82e161f4581430'
    },
    {
        'version': 1,
        'transaction': {
            'asset': {
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                },
                'updatable': False,
                'divisible': False,
                'id': '3df08a52-5cab-4697-83f0-b97b9f763a5f',
                'refillable': False
            },
            'conditions': [
                {
                    'owners_after': [
                        'G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM'
                    ],
                    'cid': 0,
                    'condition': {
                        'uri': 'cc: 4: 20: 3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlo: 96',
                        'details': {
                            'type_id': 4,
                            'public_key': 'G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM',
                            'signature': None,
                            'bitmask': 32,
                            'type': 'fulfillment'
                        }
                    },
                    'amount': 1
                }
            ],
            'metadata': {
                'data': {
                    'planet': 'earth'
                },
                'id': 'e8c51ce4-0ae7-4ff5-a591-6b5472332e23'
            },
            'fulfillments': [
                {
                    'input': None,
                    'owners_before': [
                        'G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM'
                    ],
                    'fulfillment': 'cf: 4: 3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlqskigHy3nfhHwW-1-PPjqbGdHkJk9kc5PLyIVLsdN5cnpHkfEXIXVMaJP90LPBmBKrXclHJNV1FERgaOMfLN0P',
                    'fid': 0
                }
            ],
            'operation': 'CREATE'
        },
        'id': '887f5ead6ab2ff82e6fd3b3089f787e15f422866e318343dd24213654837d85e'
    },
    {
        'version': 1,
        'transaction': {
            'asset': {
                'refillable': False,
                'updatable': False,
                'divisible': False,
                'id': '16f0a24d-4c1c-4cfc-9ef9-37c3cdcbc390',
                'data': {
                    'bicycle': {
                        'manufacturer': 'bkfab',
                        'serial_number': 'abcd1234'
                    }
                }
            },
            'conditions': [
                {
                    'owners_after': [
                        'DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'
                    ],
                    'condition': {
                        'uri': 'cc: 4: 20: t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiA: 96',
                        'details': {
                            'type_id': 4,
                            'signature': None,
                            'type': 'fulfillment',
                            'bitmask': 32,
                            'public_key': 'DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'
                        }
                    },
                    'cid': 0,
                    'amount': 1
                }
            ],
            'metadata': {
                'data': {
                    'planet': 'earth'
                },
                'id': '6ee15b26-4746-439b-878b-80789fa4506b'
            },
            'fulfillments': [
                {
                    'input': None,
                    'owners_before': [
                        'DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'
                    ],
                    'fulfillment': 'cf: 4: t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiCfrlhNlfqc5TUF9NmuWYRpZkRxFUNoFbObI6k0T5w6m9DgDyJGQU7iOJV2mefo40P_nNJuJmQWwlLXM02OIpwH',
                    'fid': 0
                }
            ],
            'operation': 'CREATE'
        },
        'id': 'aec0c7d342b0c1354190b5f3ebe8b747df63398a1c59ec5be652b0f7fad53b8a'
    }
]

rank 3 :Get block [{'id': '7858420600dc8adc991491e49d93006d38b9cdc655f62eacaa1a6b745e438231', 'transaction': {'fulfillments': [{'fid': 0, 'fulfillment': 'cf:4:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKodWMC0w9kkRFIvmw9AOSvTGdu4YR6KOYN_Y8oWsEinumNNpf8YD8mYPTn0zjzjA4iVnyh_9EKckbmOkED88YcF', 'owners_before': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs'], 'input': None}], 'conditions': [{'owners_after': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs'], 'amount': 1, 'cid': 0, 'condition': {'uri': 'cc:4:20:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKo:96', 'details': {'bitmask': 32, 'public_key': '3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs', 'type': 'fulfillment', 'signature': None, 'type_id': 4}}}], 'metadata': {'data': {'planet': 'earth'}, 'id': '372f2c14-fbbd-4cb5-90db-6713610f45e2'}, 'operation': 'CREATE', 'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'refillable': False, 'id': '5f811a71-a02e-45fd-82b2-e29264cc6c37'}}, 'version': 1}, {'id': '62f607164b394c540219996152e56235eee328add973d1d7ba82e161f4581430', 'transaction': {'fulfillments': [{'fid': 0, 'fulfillment': 'cf:4:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04_NngxF-Z9e4s8F78cLr7MZ4TVmO7ezS_WtZFJ2-3TjQWEHL_q36kB0BGW1KR6u3A8CUthRyTWEbFKjeoW9Q8I', 'owners_before': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw'], 'input': None}], 'conditions': [{'owners_after': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw'], 'amount': 1, 'cid': 0, 'condition': {'uri': 'cc:4:20:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04:96', 'details': {'bitmask': 32, 'public_key': 'C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw', 'type': 'fulfillment', 'signature': None, 'type_id': 4}}}], 'metadata': {'data': {'planet': 'earth'}, 'id': '5d072559-51c0-45e1-bf2f-a4b604b3cffb'}, 'operation': 'CREATE', 'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'refillable': False, 'id': '5108d68e-3386-487d-a5ca-bfcf068a7727'}}, 'version': 1}, {'id': '887f5ead6ab2ff82e6fd3b3089f787e15f422866e318343dd24213654837d85e', 'transaction': {'fulfillments': [{'fid': 0, 'fulfillment': 'cf:4:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlqskigHy3nfhHwW-1-PPjqbGdHkJk9kc5PLyIVLsdN5cnpHkfEXIXVMaJP90LPBmBKrXclHJNV1FERgaOMfLN0P', 'owners_before': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM'], 'input': None}], 'conditions': [{'owners_after': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM'], 'amount': 1, 'cid': 0, 'condition': {'uri': 'cc:4:20:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlo:96', 'details': {'bitmask': 32, 'public_key': 'G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM', 'type': 'fulfillment', 'signature': None, 'type_id': 4}}}], 'metadata': {'data': {'planet': 'earth'}, 'id': 'e8c51ce4-0ae7-4ff5-a591-6b5472332e23'}, 'operation': 'CREATE', 'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'refillable': False, 'id': '3df08a52-5cab-4697-83f0-b97b9f763a5f'}}, 'version': 1}, {'id': 'aec0c7d342b0c1354190b5f3ebe8b747df63398a1c59ec5be652b0f7fad53b8a', 'transaction': {'fulfillments': [{'fid': 0, 'fulfillment': 'cf:4:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiCfrlhNlfqc5TUF9NmuWYRpZkRxFUNoFbObI6k0T5w6m9DgDyJGQU7iOJV2mefo40P_nNJuJmQWwlLXM02OIpwH', 'owners_before': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'], 'input': None}], 'conditions': [{'owners_after': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'], 'amount': 1, 'cid': 0, 'condition': {'uri': 'cc:4:20:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiA:96', 'details': {'bitmask': 32, 'type_id': 4, 'type': 'fulfillment', 'signature': None, 'public_key': 'DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'}}}], 'metadata': {'data': {'planet': 'earth'}, 'id': '6ee15b26-4746-439b-878b-80789fa4506b'}, 'operation': 'CREATE', 'asset': {'updatable': False, 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'refillable': False, 'id': '16f0a24d-4c1c-4cfc-9ef9-37c3cdcbc390'}}, 'version': 1}]
rank 3 :Get votes {0, 2, 4, 6, 8, 10, 12}
rank 0 :Get block [{'transaction': {'fulfillments': [{'fid': 0, 'input': None, 'fulfillment': 'cf:4:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKodWMC0w9kkRFIvmw9AOSvTGdu4YR6KOYN_Y8oWsEinumNNpf8YD8mYPTn0zjzjA4iVnyh_9EKckbmOkED88YcF', 'owners_before': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs']}], 'asset': {'updatable': False, 'refillable': False, 'id': '5f811a71-a02e-45fd-82b2-e29264cc6c37', 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'divisible': False}, 'operation': 'CREATE', 'conditions': [{'condition': {'details': {'type': 'fulfillment', 'bitmask': 32, 'signature': None, 'public_key': '3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs', 'type_id': 4}, 'uri': 'cc:4:20:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKo:96'}, 'cid': 0, 'amount': 1, 'owners_after': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs']}], 'metadata': {'id': '372f2c14-fbbd-4cb5-90db-6713610f45e2', 'data': {'planet': 'earth'}}}, 'id': '7858420600dc8adc991491e49d93006d38b9cdc655f62eacaa1a6b745e438231', 'version': 1}, {'transaction': {'fulfillments': [{'fid': 0, 'input': None, 'fulfillment': 'cf:4:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04_NngxF-Z9e4s8F78cLr7MZ4TVmO7ezS_WtZFJ2-3TjQWEHL_q36kB0BGW1KR6u3A8CUthRyTWEbFKjeoW9Q8I', 'owners_before': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw']}], 'asset': {'updatable': False, 'refillable': False, 'id': '5108d68e-3386-487d-a5ca-bfcf068a7727', 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}}, 'operation': 'CREATE', 'conditions': [{'condition': {'details': {'type': 'fulfillment', 'bitmask': 32, 'signature': None, 'public_key': 'C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw', 'type_id': 4}, 'uri': 'cc:4:20:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04:96'}, 'cid': 0, 'amount': 1, 'owners_after': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw']}], 'metadata': {'id': '5d072559-51c0-45e1-bf2f-a4b604b3cffb', 'data': {'planet': 'earth'}}}, 'id': '62f607164b394c540219996152e56235eee328add973d1d7ba82e161f4581430', 'version': 1}, {'transaction': {'fulfillments': [{'fid': 0, 'input': None, 'fulfillment': 'cf:4:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlqskigHy3nfhHwW-1-PPjqbGdHkJk9kc5PLyIVLsdN5cnpHkfEXIXVMaJP90LPBmBKrXclHJNV1FERgaOMfLN0P', 'owners_before': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM']}], 'asset': {'updatable': False, 'refillable': False, 'id': '3df08a52-5cab-4697-83f0-b97b9f763a5f', 'divisible': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}}, 'operation': 'CREATE', 'conditions': [{'condition': {'details': {'type': 'fulfillment', 'bitmask': 32, 'signature': None, 'public_key': 'G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM', 'type_id': 4}, 'uri': 'cc:4:20:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlo:96'}, 'cid': 0, 'amount': 1, 'owners_after': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM']}], 'metadata': {'id': 'e8c51ce4-0ae7-4ff5-a591-6b5472332e23', 'data': {'planet': 'earth'}}}, 'id': '887f5ead6ab2ff82e6fd3b3089f787e15f422866e318343dd24213654837d85e', 'version': 1}, {'transaction': {'fulfillments': [{'fid': 0, 'input': None, 'fulfillment': 'cf:4:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiCfrlhNlfqc5TUF9NmuWYRpZkRxFUNoFbObI6k0T5w6m9DgDyJGQU7iOJV2mefo40P_nNJuJmQWwlLXM02OIpwH', 'owners_before': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3']}], 'asset': {'updatable': False, 'id': '16f0a24d-4c1c-4cfc-9ef9-37c3cdcbc390', 'refillable': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'divisible': False}, 'operation': 'CREATE', 'conditions': [{'condition': {'details': {'type': 'fulfillment', 'bitmask': 32, 'signature': None, 'public_key': 'DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3', 'type_id': 4}, 'uri': 'cc:4:20:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiA:96'}, 'cid': 0, 'amount': 1, 'owners_after': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3']}], 'metadata': {'id': '6ee15b26-4746-439b-878b-80789fa4506b', 'data': {'planet': 'earth'}}}, 'id': 'aec0c7d342b0c1354190b5f3ebe8b747df63398a1c59ec5be652b0f7fad53b8a', 'version': 1}]
rank 0 :Get votes {0, 2, 4, 6, 8, 10, 12}
rank 2 :Get block [{'transaction': {'metadata': {'data': {'planet': 'earth'}, 'id': '372f2c14-fbbd-4cb5-90db-6713610f45e2'}, 'conditions': [{'cid': 0, 'condition': {'details': {'signature': None, 'type_id': 4, 'public_key': '3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs', 'bitmask': 32, 'type': 'fulfillment'}, 'uri': 'cc:4:20:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKo:96'}, 'amount': 1, 'owners_after': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs']}], 'asset': {'refillable': False, 'id': '5f811a71-a02e-45fd-82b2-e29264cc6c37', 'divisible': False, 'updatable': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}}, 'operation': 'CREATE', 'fulfillments': [{'input': None, 'owners_before': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs'], 'fid': 0, 'fulfillment': 'cf:4:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKodWMC0w9kkRFIvmw9AOSvTGdu4YR6KOYN_Y8oWsEinumNNpf8YD8mYPTn0zjzjA4iVnyh_9EKckbmOkED88YcF'}]}, 'version': 1, 'id': '7858420600dc8adc991491e49d93006d38b9cdc655f62eacaa1a6b745e438231'}, {'transaction': {'metadata': {'data': {'planet': 'earth'}, 'id': '5d072559-51c0-45e1-bf2f-a4b604b3cffb'}, 'conditions': [{'cid': 0, 'condition': {'details': {'signature': None, 'type_id': 4, 'public_key': 'C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw', 'bitmask': 32, 'type': 'fulfillment'}, 'uri': 'cc:4:20:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04:96'}, 'amount': 1, 'owners_after': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw']}], 'asset': {'refillable': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'id': '5108d68e-3386-487d-a5ca-bfcf068a7727', 'updatable': False, 'divisible': False}, 'operation': 'CREATE', 'fulfillments': [{'input': None, 'owners_before': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw'], 'fid': 0, 'fulfillment': 'cf:4:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04_NngxF-Z9e4s8F78cLr7MZ4TVmO7ezS_WtZFJ2-3TjQWEHL_q36kB0BGW1KR6u3A8CUthRyTWEbFKjeoW9Q8I'}]}, 'version': 1, 'id': '62f607164b394c540219996152e56235eee328add973d1d7ba82e161f4581430'}, {'transaction': {'metadata': {'data': {'planet': 'earth'}, 'id': 'e8c51ce4-0ae7-4ff5-a591-6b5472332e23'}, 'conditions': [{'cid': 0, 'condition': {'details': {'signature': None, 'type_id': 4, 'public_key': 'G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM', 'bitmask': 32, 'type': 'fulfillment'}, 'uri': 'cc:4:20:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlo:96'}, 'amount': 1, 'owners_after': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM']}], 'asset': {'refillable': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}, 'id': '3df08a52-5cab-4697-83f0-b97b9f763a5f', 'updatable': False, 'divisible': False}, 'operation': 'CREATE', 'fulfillments': [{'input': None, 'owners_before': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM'], 'fid': 0, 'fulfillment': 'cf:4:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlqskigHy3nfhHwW-1-PPjqbGdHkJk9kc5PLyIVLsdN5cnpHkfEXIXVMaJP90LPBmBKrXclHJNV1FERgaOMfLN0P'}]}, 'version': 1, 'id': '887f5ead6ab2ff82e6fd3b3089f787e15f422866e318343dd24213654837d85e'}, {'transaction': {'metadata': {'data': {'planet': 'earth'}, 'id': '6ee15b26-4746-439b-878b-80789fa4506b'}, 'conditions': [{'cid': 0, 'condition': {'details': {'signature': None, 'type_id': 4, 'public_key': 'DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3', 'bitmask': 32, 'type': 'fulfillment'}, 'uri': 'cc:4:20:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiA:96'}, 'amount': 1, 'owners_after': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3']}], 'asset': {'refillable': False, 'id': '16f0a24d-4c1c-4cfc-9ef9-37c3cdcbc390', 'divisible': False, 'updatable': False, 'data': {'bicycle': {'manufacturer': 'bkfab', 'serial_number': 'abcd1234'}}}, 'operation': 'CREATE', 'fulfillments': [{'input': None, 'owners_before': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'], 'fid': 0, 'fulfillment': 'cf:4:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiCfrlhNlfqc5TUF9NmuWYRpZkRxFUNoFbObI6k0T5w6m9DgDyJGQU7iOJV2mefo40P_nNJuJmQWwlLXM02OIpwH'}]}, 'version': 1, 'id': 'aec0c7d342b0c1354190b5f3ebe8b747df63398a1c59ec5be652b0f7fad53b8a'}]
rank 2 :Get votes {0, 2, 4, 6, 8, 10, 12}
rank 1 :Get block [{'transaction': {'asset': {'refillable': False, 'updatable': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'id': '5f811a71-a02e-45fd-82b2-e29264cc6c37', 'divisible': False}, 'conditions': [{'owners_after': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs'], 'condition': {'uri': 'cc:4:20:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKo:96', 'details': {'signature': None, 'type_id': 4, 'bitmask': 32, 'public_key': '3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs', 'type': 'fulfillment'}}, 'cid': 0, 'amount': 1}], 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:JlgfX2AffsPWek6OcP4NI7adfHOtSwekwlh1kfz0EKodWMC0w9kkRFIvmw9AOSvTGdu4YR6KOYN_Y8oWsEinumNNpf8YD8mYPTn0zjzjA4iVnyh_9EKckbmOkED88YcF', 'fid': 0, 'owners_before': ['3agRrd5zP2keq5jQnVU6pfLFvXcjYK2ctqvFLPQxEcbs']}], 'operation': 'CREATE', 'metadata': {'data': {'planet': 'earth'}, 'id': '372f2c14-fbbd-4cb5-90db-6713610f45e2'}}, 'version': 1, 'id': '7858420600dc8adc991491e49d93006d38b9cdc655f62eacaa1a6b745e438231'}, {'transaction': {'asset': {'refillable': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'updatable': False, 'divisible': False, 'id': '5108d68e-3386-487d-a5ca-bfcf068a7727'}, 'conditions': [{'owners_after': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw'], 'condition': {'uri': 'cc:4:20:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04:96', 'details': {'signature': None, 'type_id': 4, 'bitmask': 32, 'public_key': 'C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw', 'type': 'fulfillment'}}, 'cid': 0, 'amount': 1}], 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:pbBJ8celMc2wUTHUcnXmscfZdwO0-ndIr4n0nDE5Z04_NngxF-Z9e4s8F78cLr7MZ4TVmO7ezS_WtZFJ2-3TjQWEHL_q36kB0BGW1KR6u3A8CUthRyTWEbFKjeoW9Q8I', 'fid': 0, 'owners_before': ['C9nBVUiPdQoNTd51RNMK2XHzFbMW589qMRFU9dwFpNFw']}], 'operation': 'CREATE', 'metadata': {'data': {'planet': 'earth'}, 'id': '5d072559-51c0-45e1-bf2f-a4b604b3cffb'}}, 'version': 1, 'id': '62f607164b394c540219996152e56235eee328add973d1d7ba82e161f4581430'}, {'transaction': {'asset': {'refillable': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'updatable': False, 'divisible': False, 'id': '3df08a52-5cab-4697-83f0-b97b9f763a5f'}, 'conditions': [{'owners_after': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM'], 'condition': {'uri': 'cc:4:20:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlo:96', 'details': {'signature': None, 'type_id': 4, 'bitmask': 32, 'public_key': 'G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM', 'type': 'fulfillment'}}, 'cid': 0, 'amount': 1}], 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:3w6YcUdmDNchncjjmkQNhXWfu4XxnhCreRbicekjSlqskigHy3nfhHwW-1-PPjqbGdHkJk9kc5PLyIVLsdN5cnpHkfEXIXVMaJP90LPBmBKrXclHJNV1FERgaOMfLN0P', 'fid': 0, 'owners_before': ['G1ipr1zrWBcdwtUtDhKm8DxvDh5tyqpEgD4Y15zT5TkM']}], 'operation': 'CREATE', 'metadata': {'data': {'planet': 'earth'}, 'id': 'e8c51ce4-0ae7-4ff5-a591-6b5472332e23'}}, 'version': 1, 'id': '887f5ead6ab2ff82e6fd3b3089f787e15f422866e318343dd24213654837d85e'}, {'transaction': {'asset': {'refillable': False, 'updatable': False, 'data': {'bicycle': {'serial_number': 'abcd1234', 'manufacturer': 'bkfab'}}, 'id': '16f0a24d-4c1c-4cfc-9ef9-37c3cdcbc390', 'divisible': False}, 'conditions': [{'owners_after': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3'], 'condition': {'uri': 'cc:4:20:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiA:96', 'details': {'signature': None, 'type_id': 4, 'type': 'fulfillment', 'public_key': 'DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3', 'bitmask': 32}}, 'cid': 0, 'amount': 1}], 'fulfillments': [{'input': None, 'fulfillment': 'cf:4:t40glmy_0IY9f-9U_ApWtF21gShBBvgsoj-aIc1bYiCfrlhNlfqc5TUF9NmuWYRpZkRxFUNoFbObI6k0T5w6m9DgDyJGQU7iOJV2mefo40P_nNJuJmQWwlLXM02OIpwH', 'fid': 0, 'owners_before': ['DMWRVuX5qYDvK6bjBkGWNQbbmJ4k5BfWriH2c89eVFQ3']}], 'operation': 'CREATE', 'metadata': {'data': {'planet': 'earth'}, 'id': '6ee15b26-4746-439b-878b-80789fa4506b'}}, 'version': 1, 'id': 'aec0c7d342b0c1354190b5f3ebe8b747df63398a1c59ec5be652b0f7fad53b8a'}]
rank 1 :Get votes {0, 2, 4, 6, 8, 10, 12}
```
