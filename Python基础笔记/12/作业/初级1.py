# 1.刘凯买了一台玫瑰红phone10，价值8000元，可以打电话、玩游戏
# class Person():
#     def __init__(self,name):
#         self.name = name
#     def use(self):
#         print("使用",phone.colour,phone.name)
#         return phone.game()
# class Phone():
#     def __init__(self,name,colour,money):
#         self.name = name
#         self.colour = colour
#         self.money = money
#     def call(self):
#         return '打电话'
#     def game(self):
#         return '玩游戏'
# person = Person('刘凯')
# phone = Phone('iphone10','玫瑰红','8000元')
# print(person.name)
# print(person.use())

class Person:
    def __init__(self,name):
        self.name = name
    def buy(self,phton):
        print("{}买了{}".format(self.name,phton.brand))
class Phone:
    def __init__(self,brand,colour,price):
        self.brand = brand
        self.colour = colour
        self.price = price
    def call(self):
        print("打电话")
    def game(self):
        print("玩游戏")
phone = Phone('iphton10','玫瑰红',8000)
liukai = Person("刘凯")
liukai.buy(phone)













