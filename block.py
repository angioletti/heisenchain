import time

class Block:
    def __init__(self):
        self.index = None
        self.transaction_list = []
        self.create_timestamp = time.time()
        self.previous_hash = None
        self.nonce = ''
        self.hash = ''

    def __repr__(self):
        # FIXIT: this repr doesn't make much sense
        prn = [self.index, self.transaction_list, ]
        return (str(self.index) + str(self.transaction_list) + str(self.create_timestamp)
                     + str(self.previous_hash) + str(self.nonce))

    def add_transac(self, transac):
        self.transaction_list.append(transac)
