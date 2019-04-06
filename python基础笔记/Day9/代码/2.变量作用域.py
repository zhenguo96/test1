# 变量作用域:能够引用变量的代码段就叫这个变量的作用域
# 1 if while for-in try-except这些不引入新的作用域
# if 3 > 0:
#     a = 1
# print(a)
# 全局作用域：在所有的函数外定义变量
# 范围：从定义开始到本文件结束
a = 3
def demo():
    print("demo",a)
    b = 5       # 局部作用域，局部变量，范围：整个函数体，不能在定义之前引用
    print(b)
demo()
print(a)
# print(b)

# 内部函数
def test():
    c = 10      # 闭包作用域：从定义开始到本函数结束
    def inner():    #　作用域是局部作用域
        b = 10
        print("inner",b)
    inner()
# inner()       # 不能在外部引用内部函数

# 内建作用域：所有文件都可用,系统函数、变量都是内建作用域
print(max(1,2,3))

# n内建作用域 > 全局作用域 > 闭包作用域 > 局部作用域






