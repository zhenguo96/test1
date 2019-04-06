'''
3.四则计算器，从键盘输入两个数和一个运算符（+-*/）,根据运算符计算表达式的结果。
  提示：请考虑除数为0的情况
'''
num1 = float(input("数："))
op = input("运算符：")
num2 = float(input("数:"))
c = 0
if op == "+":
    c = num1 + num2
elif op == "-":
    c = num1 - num2
elif op == "*":
    c = num1 * num2
elif op == "/":
    if num1 == 0:
        print("除数不能为0")
        quit()
    else:
        c = num1 / num2
print(c)


str = input("")
a = str.split()
if a[1] == "+":
    c = int(a[0]) + int(a[2])
elif a[1] == "-":
    c = int(a[0]) - int(a[2])
elif a[1] == "*":
    c = int(a[0]) * int(a[2])
elif a[1] == "/":
    if a[0] == 0:
        print("除数不能为0")
    else:
        c = int(a[0]) / int(a[2])
print("%s %s %s = %d" % (a[0], a[1], a[2], c))









