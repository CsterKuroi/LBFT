from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

def create():
    alice = generate_keypair()
    return(alice)

if __name__=="__main__":
    print(create())
    
