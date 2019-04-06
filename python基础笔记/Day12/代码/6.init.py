# # 如果你不定义__inti__，系统会自动生成
# class Cat:
#     """
#     猫类
#     """
#     pass
#     """
#     def __init__(self):
#         pass
#     """
# cat = Cat()
# # 查看类所有的方法和属性
# print(dir(Cat))
# print(Cat.__doc__)


class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 会覆盖一个构造方法
    def __init__(self,name,age,blood):
        self.name = name
        self.age = age
        self.blood = blood
c1 = Cat('猫',3,1000)
print(c1.name)


