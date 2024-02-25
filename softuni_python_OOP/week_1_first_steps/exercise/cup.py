class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity


    def fill(self, given_quantity):
        if self.size - self.quantity >= given_quantity:
            self.quantity += given_quantity


    def status(self):
        return self.size - self.quantity

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
