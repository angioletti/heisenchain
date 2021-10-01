import blockchain as bch
import time
import block as blk
import transaction as trn
import product as prd

class Miner:
    def __init__(self, blockchain, block):
        self.bchain = blockchain
        self.block = block

    def bundle_pending_transactions(self, self.block):
        for index, i in enumerate(self.bchain.pool_transaction):
            self.operate_transac(i, index)
            block.add_transac(i)
            bchain.pool_transaction.pop(index)

    def validate_coverage(self,transac):
        if transac.trtype != 'create' and transac.sender.products[product] >= quantity:
            return True
        else:
            print("Insufficient funds to cover the transaction.")
            return False

    def operate_transac(self,transac,index):
        transac.coverage = validate_coverage(transac)
        if transac.coverage == True:
            if transac.trtype = 'create':
                transac.receipt.add_resources(transac.product, transac.quantity)
            else:
                transac.sender.subtract_resources(transac.product, transac.quantity)
                transac.receipt.add_resources(transac.product, transac.quantity)
        else:
            bchain.pool_transaction.pop(index)
            bchain.pool_rejected_transac.append(transac)

    def compute_hash(self, block):
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
