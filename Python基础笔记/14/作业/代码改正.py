class Dog(object):
    def __init__(self, name):
        self.name = name
    @property
    def eat(self):
        print(" %s is eating" % self.name)
d = Dog("ChenRonghua")
d.eat



