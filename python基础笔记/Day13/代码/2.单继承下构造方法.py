class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        self._a = 10    # 保护属性直接使用
    def eat(self):
        print("吃")
    def get_age(self):
        return self.__age
class Dog(Animal):
    def __init__(self,name,age,kind):
        # 继承自父类的属性可以调用父类的构造方法初始化
        # super(Dog,self).__init__(name)
        # super().__init__(name)
        Animal.__init__(self,name,age)      # 不推荐
        # self.age = age
        self.kind = kind
    def t1(self):
        # 继承自父类的私有属性不能够在子类中直接引用
        # print(self.__age)
        print(self.get_age())
        # 保护属性直接使用
        # print(self._p)
        # 改写继承父类的方法
    def eat(self):
         # 调用继承父类的方法
        super().eat()
        print("爱吃")
        # 新增方法
    def bark(self):
        print("www")
jinmao = Dog("dd",18,"金毛")
print(jinmao.__dict__)
print(jinmao.name)
# 子类对象会优先调用子类改写的方法
jinmao.eat()










