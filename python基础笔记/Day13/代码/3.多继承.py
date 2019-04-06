# # 多继承
# class Base1:
#     def __init__(self,name):
#         self.name = name
#     def t1(self):
#         print("Base1")
#
# class Base2:
#     def __init__(self,name):
#         self.name = name
#     def t2(self):
#         print("Base2")
#
# class Base3:
#     def __init__(self, name):
#         self.name = name
#     def t3(self):
#         print("Base3")
#
# # 多继承的子类
# class Child(Base1,Base2,Base3):
#     pass
# child = Child('tom')
# print(child.__dict__)
# child.t1()
# child.t2()
# # 继承顺序
# print(Child.mro())
# print(Child.__mro__)
#







