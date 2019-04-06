# from collections import deque
# import os
# queue = deque()
# queue.append(r'E:\千锋课堂资料\Day16\代码')
# # print(len(queue))
# top = queue.pop()
# # print(top)
# d = os.listdir(top)
# # print(d)
# for items in d:
#     tem = os.path.join(top,items)
#     print(tem)

# a = [1,2,3,4]
# s1 = "abcdef"
# c = (9,8,7,3)
# res = set(zip(a,s1,c))
# print(res)
# for value in res:
#     print(value)
#=>dict
# res = dict(zip(s1,c))
# print(res)


# s1 = "helloowooweioei"
# print(list(s1))
# print(len(list(s1)))

# class A:
#     __num = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__num is None:
#             cls.__num = super().__new__(cls, *args, **kwargs)
#         return cls.__num
#     def eat(self):
#         print("*"*50)
# a = A()
# a2 = A()
# print(id(a),id(a2))
# a.eat()

# class A:
#     def __call__(self,func,*args,**kwargs):
#         def inner():
#             func()
#             print("*"*50)
#         return inner
# @A()
# def eat():
#     print("----------------------------")
# eat()
# a = 1

# a = [1,2,3]
# print("".join(a))

# a = '1ab3'
# for i in a:
#     print(i.isalpha())


#

# a = {'a':1,'b':2}
# b = {}
# for key,value in a.items():
#     b[value]=key
# print(b)























