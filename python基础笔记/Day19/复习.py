# def demo():
#     pass
# class Pig:
#     def __call__(self, *args, **kwargs):
#         print("go go go!")
#         print(args,kwargs)
#
# p1 = Pig()
# p1(10,a=6)
# # callable测试一个对象是否可调用
# print(callable(p1))
# print(callable(demo))
#
# class Decrator:
#     def __call__(self, func1):
#         def inner():
#             func1()
#             print("*"*50)
#         return inner
# @Decrator()
# def test1():
#     print("类装饰器")
# test1()

# class Fib:
#     def __init__(self):
#         self.x = 0
#         self.y = 1
#     def __iter__(self):
#         return  self  #返回当前对象
#     def __next__(self):
#         self.x ,self.y = self.y, self.x + self.y   #迭代公式
#         if self.x > 1000:
#             raise StopIteration()
#         return  self.x
# f = Fib()
# print([x for x in f ])

# class A:
#     pass
# class B(A):
#     pass
# b = B()
# print(issubclass(b,B))
# print(issubclass(A,B))
# print(issubclass(b,A))

class MyInt:
    def __init__(self,num):
        self.num = num
    def __rsub__(self, other):
        return MyInt(other - self.num )
    # 重载减法运算符
    def __sub__(self, other):
        return MyInt(self.num - other.num)
    #重载加法运算符
    def __add__(self, other):
        return MyInt(self.num + other.num)
    # def add(self,other):
    #     return MyInt(self.num + other.num)
    # 关系运算符
    # def __lt__(self, other):
    #     return self.num < other.num
    def __str__(self):
        return str(self.num)
a = MyInt(2)
b = MyInt(5)
# print(a + b)  # a.__add__(b)
# print(a - b)  # a.__sub__(b)
# print(3 - b)  # b.__rsub__(3)
# print(a < b)
# print(a.add(b))
list1 = [MyInt(10),MyInt(15),MyInt(9)]
# list1.sort(reverse=True)
list1.sort(key=lambda x:x.num,reverse=True)
for item in list1:
    print(item)









