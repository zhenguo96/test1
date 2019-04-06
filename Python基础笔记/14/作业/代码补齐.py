class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print("要不死你就是我大爷")
    def set_age(self,age):
        self.age = age
        return self.age
    def __str__(self):
        return "我是{}，今年{}岁".format(self.name,self.age)
td = Dog("泰迪", 5)
print(td.name)
td.set_age(3)
print(td)  # 输出：我是泰迪，今年3岁
td.bark()