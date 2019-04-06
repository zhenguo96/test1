# class Person:
#     male_num = 0
#     __female_num = 0
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.__age = age
#         self.sex = sex
#         if self.sex in ['男','m','1']:
#             self.__class__.male_num += 1
#         else:
#             self.__class__.__female_num += 1
#     @property   # 方法属性化，get方法
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if value < 0:
#             raise ValueError("年龄不能小于0")
#         else:
#             self.__age = value
#     @classmethod
#     def get_femal_num(cls):
#         return cls.__female_num
#     # def get_age(self):
#     #     return self.__age
#     def __str__(self):
#         return "{} {} {}".format(self.name,self.__age,self.sex)
#     def think(self):
#         print("思考")
#         # self.__kiss()
#         return self
#     def __kiss(self):
#         print("kiss")
#     def __del__(self):
#         print("del")
#         if self.sex in ['男','m','1']:
#             self.__class__.male_num -= 1
#         else:
#             self.__class__.__female_num -= 1
# tom = Person("tom",18,"男")
# # print(tom.__dict__)
# # print(tom.name)
# # print(tom.__age)
# # print(tom.age)
# # print(tom)
# # tom.think().think()
# # 动态增加对象属性
# # tom.male_num = 10
# Person.male_num = 18

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def __call__(self, *args, **kwargs):
        print("可调用")
    def eat(self):
        return "吃"

class JinMao(Dog):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender = gender
    def eat(self):
        return super().eat()
jm = JinMao("aaa",3,"男")
# print(jm.eat())
print(jm.eat())











