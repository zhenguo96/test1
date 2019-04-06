class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("吃")
class Cow(Animal):
    def eat(self):
        print("吃的是草，挤得是奶")

cow = Cow("奶牛")




















