class Animal():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def caiyi(self, caiyi):
        print("昵称是：{}，年龄是：{}，性别：{}".format(self.name,self.age,self.gender))
        print("会{}的才艺".format(caiyi))

class Dog(Animal):
    pass

class Mao(Animal):
    pass

dog = Dog("贝贝",2,"雌")
dog.caiyi("两条腿行走")
mao = Mao("花花",1,"雄")
mao.caiyi("装死")






