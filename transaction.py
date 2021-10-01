import time

class Transaction:

    allowed_transactions = ['create', 'transfer', 'remove']

    def __init__(self, blockchain, trtype, product, quantity,
                 sender, recepient, details):

        if trtype not in allowed_transactions:
            print('Unable to create transaction type: ' + trtype)
            return None
        else:
            self.blockchain = blockchain
            self.product = product
            self.quantity = quantity
            self.details = details
            self.sender = sender
            self.recepient = recepient
            self.create_timestamp = time.time()
            self.transac_id = self.transac_id()


        def transac_id():
            id_seed = [self.product.id, self.quantity, self.details,
                       self.recepient, self.sender, self.timestamp]
            transac_id = hl.sha1(repr(id_seed).encode()).hexdigest()
            return transac_id

