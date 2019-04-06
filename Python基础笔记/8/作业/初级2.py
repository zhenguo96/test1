# 2. 写函数，传入一个参数n，返回n的阶乘
def jiecheng(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a
res = jiecheng(3)
print(res)














