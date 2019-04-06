# 2.自己定义一个列表的操作类，完成：
# - 自定义构造方法，__init__(self,*args)可以传入多个元素，存入自定义列表
# - 定义append(self,value),将指定元素value添加到列表
# - 定义get(self,index),index是下标，如果下标越界终止程序，否则返回对应元素值
# - 定义pop(self,index=-1)，如果不传参数删除最后一个元素并返回去其值，否则删除下标index指定的元素
# class List1():
#     def __init__(self,*args):
#         self.li = list(args)
#     def append(self,value):
#         self.li.append(value)
#         return self.li
#     def get(self,index):
#         if len(self.li) - 1 < index:
#             return "下标越界"
#         return self.li[index]
#     def pop(self,index=-1):
#         return self.li.pop(index)
# l = List1(2,45,4,31,12)
# print(l.append(11))
# print(l.get(1))
# print(l.pop())

# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return self.a + self.b
#     def sub(self):
#         return self.a - self.b
#     def mul(self):
#         return self.a * self.b
#     def div(self):
#         if self.b < 0 or self.b > 0:
#             return self.a / self.b
#         return Exception("除数不能为0")
# cal = Calculator(2,3)
# # cal = 90
# print(cal.add())
# cal.b = 0
# cal.div()

class Calculator:
    a = 2
    @staticmethod
    def add(cls,a,b):
        return a + b
    @staticmethod
    def sub(ls,a,b):
        return a - b
    @staticmethod
    def mul(ls,a,b):
        return a * b
    @staticmethod
    def div(ls,a,b):
        if b <0 or b >0:
            return a/b
        print("除数不能为0")
    @staticmethod
    def power(a):
        print(Calculator.add(2,3))
print(Calculator.add(4,5))
Calculator.power(3,4)

