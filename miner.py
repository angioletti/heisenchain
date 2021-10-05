import blockchain as bch
import time
import json
import hashlib as hl
import block as blk
import transaction as trn
import product as prd

class Miner:
    def __init__(self, blockchain):
        self.bchain = blockchain
        self.block = blk.Block()

    def bundle_pending_transactions(self):
        for index, i in enumerate(self.bchain.pool_transaction):
            self.operate_transac(i, index)
            print("Processing transaction " + str(index) + ": " + str(i))
        self.bchain.pool_transaction = []

    def validate_coverage(self,transac):
        if transac.sender.check_balance(transac.product) >= transac.quantity:
            return True
        else:
            print("Insufficient funds to cover the transaction.")
            return False

    def operate_transac(self,transac,index):
        if transac.trtype == 'create':
            transac.recepient.add_resource(transac.product, transac.quantity)
            self.block.add_transac(transac)
            self.bchain.pool_transaction.pop(index)
        elif transac.trtype == 'remove':
            transac.coverage = self.validate_coverage(transac)
            if transac.coverage == True:
                transac.recepient.subtract_resource(transac.product, transac.quantity)
                self.block.add_transac(transac)
                self.bchain.pool_transaction.pop(index)
        elif transac.trtype == 'transfer':
            transac.coverage = self.validate_coverage(transac)
            if transac.coverage == True:
                transac.recepient.add_resource(transac.product, transac.quantity)
                transac.sender.subtract_resource(transac.product, transac.quantity)
                self.block.add_transac(transac)
                self.bchain.pool_transaction.pop(index)
        else:
            self.bchain.pool_transaction.pop(index)
            self.bchain.pool_rejected_transaction.append(transac)

    def compute_hash(self):
        bstring = repr(self.block)
        bhash = hl.sha256(bstring.encode()).hexdigest()
        return bhash

    def validate_block(self):
        '''
        Validates a block by computing a valid hash and, through that,
        providing a proof of work type of consensus.
        There is no protocol implemented yet to accommodate multiple miners.
        Returns a tuple with valid hash and its nonce.
        '''
        self.block.nonce = 0
        valid_hash = ''
        while not valid_hash.startswith('0' * self.bchain.difficulty):
            valid_hash = self.compute_hash()
            self.block.nonce += 1
        self.block.hash, self.block.nonce = (valid_hash, self.block.nonce - 1)
        print("Block {} validated and sent to blockchain for inclusion".format(self.block.hash[:8]))
        self.bchain.pool_unconfirmed_block.append(self.block)
