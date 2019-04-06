# 1.对加减乘除分别封装一个函数进行计算，参数是两个数，返回值是计算结果
choise = int(input("选择1.+, 2.-, 3.*, 4./, 0.退出:"))
if choise == 0:
    quit()
num1 = int(input("第一个数："))
num2 = int(input("第二个数："))
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if num1 == 0:
        return "除数不能为0"
    return a / b
a = [0,add,sub,mul,div]
if 0 <= choise <= 4:
    print(a[choise](num1,num2))





