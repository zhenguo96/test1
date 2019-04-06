# 在函数里无法直接修改全局变量
a = 5
def test1():
    global a    # 告诉python解释器，以下引用的是全局变量，并且可以修改
    a = 10      # 全局变量
    print(a)
test1()
print(a)
def outter():
    c = 10          # 闭包作用域
    def inner():
        nonlocal c
        c += 1  # 不允许直接修改闭包作用域
        print(c)
    inner()
outter()






