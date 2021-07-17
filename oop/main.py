class Address:
    stream = 'csc'
    def __init__(self):
        pass

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return  self.address


a = Address()
a.set_address("tayorgudestryhero");
print(a.get_address())


