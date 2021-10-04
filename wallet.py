import hashlib as hl
import time

class Wallet:
    '''
    Object that retains balances for users.
    Each new user instantiates a new wallet from scratch and adds balance to it.
    That balance will be use to validate that the user has enough resources to
    operate in transactions.

    arguments:  none
    returns  :  wallet object with a wallet_id, its products and their respective balances.

    To manipulate the products in a wallet, specific methods have to be used
    '''
    def __init__(self, blockchain):
        self.product_dict = dict()
        self.wallet_id = self.wallet_id()
        self.blockchain = blockchain

    def wallet_id(self):
        wallet_id = hl.sha1(repr(str(time.time())).encode()).hexdigest()
        return wallet_id

    def add_resource(self, product, amount):
        if product.id in [x for x in self.product_dict.keys()]:
            self.product_dict[product.id] += amount
        else:
            self.product_dict[product.id] = amount


    def subtract_resource(self, product, amount):
        if product.id not in [x for x in self.product_dict.keys()] \
                or self.product_dict[product.id] < amount:
            print("Insufficient balance")
            return False
        else: self.product_dict[product.id] -= amount

    def __repr__(self):
        header = ['Total balance for this wallet:']
        if len(self.product_dict) == 0:
            return self.wallet_id[:4] + ": No funds!\n"
        else:
            products = ["{prd} : {qty}".format(prd=x[:6], qty=y) for x,y in self.product_dict.items()]
            return '\n'.join(header + products + ['\n'])

    def check_balance(self, product):
        if product in self.product_dict.keys():
            return product.dict[product]
        else:
            return 0

