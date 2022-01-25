class fruit(object):
    def __init__(self, fruit):
        self.fruittype = fruit[0]
        self.days = int(fruit[1])
        self.trait1 = fruit[2]
        self.trait2 = fruit[3]
    def fruittype(self):
        return self.fruittype
    def days(self):
        return self.days
    def traits(self):
        traits = [self.trait1, self.trait2]
        traits.sort()
        return traits