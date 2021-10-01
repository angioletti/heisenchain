import time

class Block:
    def __init__(self):
        self.index = None
        self.transactions = []
        self.create_timestamp = time.time()
        self.previous_hash = None
        self.nonce = ''
        self.hash = ''

    def add_transac(transac):
        if len(transac) < 11:
            self.transactions.append(transac)
            return True
        else:
            return False

