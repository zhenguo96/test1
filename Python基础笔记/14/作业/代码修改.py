class Cat:
    def __init__(self,name,age):
         self.name = name
         self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age
        return self.__age
    def miao(self):
        print("喵喵")
# 以下代码不能修改
bsm = Cat('加菲猫',5)
print(bsm.name,bsm.age)
bsm.name = '大肥猫'
bsm.age = 6
bsm.miao()