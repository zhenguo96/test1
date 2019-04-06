class Girl:
    def __init__(self,name,age):
        # 公有属性
        self.name = name
        # 私有属性，不能通过对象.__age调用
        self.__age = age
    # 属性装饰器     把方法变为属性
    @property
    def age(self):
        return self.__age   # 类内方法里不区分公有和私有
    # setter
    @age.setter
    def age(self,age):
        # 可以做数据校验
        if age < 0:
            print("年龄不能小于0")
        else:
            self.__age = age
anglebaby = Girl("杨颖",25)
print(anglebaby.age)
anglebaby.age = 10
print(anglebaby.age)





