import hashlib as hl

class Product:
    '''
    The actual elements that will be transacted in wallets.
    Each product has:
        - an id that is unique at the moment of its creation (SHA1)
        - a name
        - a manufacturer
    '''

    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.id = hl.sha1(repr(self.manufacturer+' '+self.name).encode()).hexdigest()

    def __repr__(self):
        product = 'Product_ID  : ' + self.id[:6]
        name = 'Name        : ' + self.name
        manuf = 'Manufacturer: ' + self.manufacturer
        return '\n'.join([product,name,manuf])
