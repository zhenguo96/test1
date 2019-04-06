def demo1(k,j):
    print(k,j)
#1.位置参数
print(demo1(1,2))

# 关键字参数（实参）
demo1(j=3,k=2)

# 3.默认值     从右向左给形参覆默认值
def demo2(a,b,c=4):
    print(a,c,b)
demo2(2,3)
demo2(3,2,1)

# 任意位置参数
def demo3(*args):
    print(*args)
demo3(1,2,3,4,1)

# 任意关键字参数
def demo4(**kwargs):
    print(kwargs)
demo4(a=3)
demo4(a=1,b=4)

a = [2,3,4]
def demo5(a):
    a[0] = 100
demo5(a)
print(a)

# 函数类型
# def demo6():
#     print("demo6")
# print(type(demo6))
# demo6 = 6
# a = demo6
# a()

# def demo7(func):
#     func()
# demo7(demo6)

pf = lambda a,b:a + b
print(pf(1,2))

def fun():
    print("aaaaaaaaaaaa")
# 闭包
def outer(func):
    a = 1
    def inner():
        func()
        print(a)
    return inner
fun = outer(fun)
fun()

a = 1
def test1():
    global a
    a += 2
    print(a)
test1()
print(a)











