##
## Blockchain class to be imported by our simulator
##

from hashlib import sha256
import transaction as trn
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
    transactions_per_block = 3

    def __init__(self):
        self.pool_unconfirmed_block = []
        self.pool_rejected_block = []
        self.pool_transaction = []
        self.pool_rejected_transaction = []
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
        genesis_block = bl.Block()
        genesis_block.nonce = 0
        genesis_block.hash = '0'*64
        print(genesis_block.hash)
        self.chain.append(genesis_block)
        print(type(self.chain[0]))

    def is_valid_hash(self, block):
        '''
        Checks that a block has been validated.
        It will use the block's nonce, hash and content
        and compare them to a calculated valid block
        '''
        nonce = block.nonce
        bhash = block.hash

        # Was not tampered with
        if bhash.startswith('0'*self.difficulty):
            not_tampered = True
        else:
            not_tampered = False

        return not_tampered

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

        if self.is_valid_hash(block):
            block.previous_hash = self.last_block.hash
            block.index = len(self.chain) - 1
            self.chain.append(block)

        else:
            print("Block not added. Check its integrity before trying again")
            self.pool_rejected_block.append(block)

        return None

    def transaction_broker(self,trtype,product,quantity,sender,recepient,details):
        '''
        This method instantiates transactions and files them to be included in blocks
        '''
        transac = trn.Transaction(trtype, product, quantity, sender, recepient, details)
        self.pool_transaction.append(transac)
#        print(self.pool_transaction)

    def query_blocks(self):
        for idx, i in enumerate(self.chain):
            print("""\n Block: {seq}\n Prev. Hash: {phash}\n Hash: {hash}\n Transactions: {trn}\n""".format(seq=idx, hash=i.hash, trn=i.transaction_list, phash=i.previous_hash))
