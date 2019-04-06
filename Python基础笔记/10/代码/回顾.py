# a = 5
# print(a)
# def outter(s):
#     b = 3
#     global a    # 全局变量声明 不添加global声明，不能修改全局变量
#     a += 2
#     print('a=',a)
#     def inner():
#         nonlocal b
#         print("b=",b)
#         c = 3
#         global a
#         a += 3
#     inner()
# outter(a)
# print(a)

def outer():
    a = 3
    def inner():    # 1 内部函数
        nonlocal a
        a += 5
        print(a)    # 2 外部变量
    print(inner)
    return inner    # 3 返回内部函数
p = outer()
print(p)
p()

# 装饰器
# def demo():
#     print("*" * 10)

# def outer(func):
#     def inner():
#         func()
#         print("*" * 10)
#         print("*" * 10)
#     return inner    # 3 返回内部函数
# tmp = outer(demo)   # 传入要修饰的函数，返回inner
# tmp()


# def outer(func):
#     def inner():
#         func()
#         print("*" * 10)
#         print("*" * 10)
#     return inner    # 3 返回内部函数
# @outer  # demo = outer(demo)
# def demo():
#     print("*" * 10)

# 带参数
def outer(func):
    # 如果带参数，inner应该和demo有相同参数
    def inner(n):    # 1 内部函数
        func(n)
        print("*" * n)
        print("*" * n)
    return inner    # 3 返回内部函数
@outer  # demo = outer(demo)
def demo(n):
    print("*" * n)



