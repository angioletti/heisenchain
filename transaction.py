import time
import hashlib as hl

class Transaction:

    allowed_transactions = ['create', 'transfer', 'remove']

    def __init__(self, trtype, product, quantity,
                 sender, recepient, details):

        if trtype not in self.allowed_transactions:
            print('Unable to create transaction type: ' + trtype)
            return None
        else:
            self.product = product
            self.quantity = quantity
            self.details = details
            self.sender = sender
            self.recepient = recepient
            self.create_timestamp = time.time()
            self.transac_id = self.transac_id()

    def __str__(self):
        return("TR-" + self.transac_id[:4])

    def __repr__(self):
        return('TR-' + self.transac_id[:4])

    def transac_id(self):
        id_seed = [self.product.id, self.quantity, self.details,
                   self.recepient, self.sender, self.create_timestamp]
        transac_id = hl.sha1(repr(id_seed).encode()).hexdigest()
        return transac_id
