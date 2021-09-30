##
## Blockchain class to be imported by our simulator
## v 0.01
## last update: 2021-09-29
##
from hashlib import sha256
import block as bl
import time
import json


class Blockchain:
    '''
    Instantiates a blockchain object.
    This object is non-persistent, meaning that each time the object is instantiated
    the blockchain will be reset
    '''
    difficulty = 2

    def __init__(self):
        self.unconfirmed_blocks = []
        self.chain = []
        self.create_genesis_block()
    
    @property
    def last_block(self):
        return self.chain[-1]

    def create_genesis_block(self):
        '''
        The genesis block is a special block, where the blockchain starts.
        It doesn't have to contain a transaction.
        It does, however, contain a nonce and a valid hash
        '''
        genesis_block = bl.(0, [], time.time(), '0')
        genesis_block.nonce = 0
        genesis_block.hash = '0'*64
        self.chain.append(genesis_block)

    def compute_hash(block):
        bstring = json.dumps(block.__dict__, sort_keys=True)
        bhash = sha256(bstring.encode()).hexdigest()
        return bhash


    def validate_block(self, block):
        '''
        Validates a block by computing a valid hash and, through that, 
        providing a proof of work type of consensus.
        There is no protocol implemented yet to accommodate multiple miners.
        Returns a tuple with valid hash and its nonce.
        '''
        block.nonce = 0
        valid_hash = ''
        while not valid_hash.startswith('0' * self.difficulty):
            valid_hash = self.compute_hash()
            block.nonce += 1
        return valid_hash, block.nonce - 1
    
    def is_valid_hash(self, block):
        '''
        Checks that a block has been validated.
        It will use the block's nonce, hash and content
        and compare them to a calculated valid block
        '''
        nonce = block.nonce
        bhash = block.hash

        # The hash has the expected form
        if bhash.startswith('0')*self.difficulty:
            looks_right = True
        else:
            looks_right = False

        # Was not tampered with
        if bhash == self.compute_hash(block):
            not_tampered = True
        else:
            not_tampered = False

        return (looks_right and not_tampered)

    def add_block(self, block):
        '''
        Adds a block to the instantiated blochchain.
        When adding a block, the blockchain makes sure that
        this block is chained to the last one present.
        It also verifies the PoW for that block.

        The block was created by an agent that groups transactions into a block
        and parks that block for validation by a miner
        The block was validated by a miner, who asks to append the block to the blockchain.
        '''
        
        if is_valid_hash(block):
            block.previous_hash = self.last_block()
            chain.append(block)
        else:
            print("Block not added. Check its integrity before trying again")

        return None


