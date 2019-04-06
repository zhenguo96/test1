#连续求和
def add(num):
    sum1 = num
    while True:
        x = yield sum1
        if isinstance(x,str):
            break
        sum1 += x
t1 = add(2)     # 创建协程对象，代码没有执行
next(t1)    # next启动代码执行到第一个yield
print(t1.send(10))























