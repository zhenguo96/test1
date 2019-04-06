#　嵌套调用
def demoA():
    print('a')
def demoB():
    print('b')
    demoA()
    print('-------b')
def demoC():
    print('C')
    demoB()#中断
    print("-----------c")
demoC()

# 递归调用
"""
5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
"""
def fac(n):
    if n == 0:  # 1.递归终止条件
        return 1
    return fac(n-1) * n     # 2.递归
fac(10)

# 练习
def demo1(n):
    if n <= 0:
        return
    print(n%10)
    demo1(n//10)
demo1(12345)





