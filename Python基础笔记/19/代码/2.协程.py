# 协程
def sub():
    print("开始")
    x = yield
    print("x = ",x)
    y = yield x + 1
    print("x = ", x, "y = ", y)
    yield

x1 = sub()
next(x1)
print(x1.send(3))
x1.send(4)
















