# 单继承 一个类只有一个父类
"""
class 类名（父类名）:
    
"""
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("吃")

class Bird(Animal):
    pass

maque = Bird('麻雀')
maque.eat()













