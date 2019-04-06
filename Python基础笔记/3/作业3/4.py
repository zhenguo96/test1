'''
4.计算面积
编写程序，由用户输入的三角形的三条边，计算三角形的面积。
解题提示：
三角形面积的计算公式为： ，其中a、b、c为三角形的三条边，l=(a+b+c)/2；考虑用户输入的三条边是否能构成三角形；
'''
num1 = float(input("第一条边长："))
num2 = float(input("第二条边长："))
num3 = float(input("第三条边长："))
if num1 < num2:
    num1, num2 = num2, num1
if num1 < num3:
    num1, num3 = num3, num1
if num2 < num3:
    num2, num3 = num3, num2
if num3 + num2 > num1 and num1 - num2 < num3:
    l = (num1 + num2 + num3) / 2
    print(l)
else:
    print("不能构成三角形")









