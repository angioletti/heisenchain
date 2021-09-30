import hashlib

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
    def __init__(self):
        self.products = dict()
        self.wallet_id = self.wallet_id()

    def wallet_id(self):
        wallet_id = hl.sha1(repr(str(time.time())).encode()).hexdigest()
        return wallet_id

    def add_resource(self, product, amount):
        if product.id in [x for x in self.products.keys()]:
            self.products[product.id] += amount
        else:
            self.products[product.id] = amount


    def subtract_resource(self, product, amount):
        if product.id not in [x for x in self.products.keys()] \
                or self.products[product.id] < amount:
            print("Insufficient balance")
            return False
        else: self.products[product.id] -= amount

    def __repr__(self):
        header = ['Total balance for this wallet:']
        products = ["{prd} : {qty}".format(prd=x[:6], qty=y) for x,y in self.products.items()]
        return '\n'.join(header + products)
