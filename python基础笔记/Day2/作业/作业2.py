# 判断下面标识符是否合法并说明不合法的原因
# abc.com             不合法，由字母数字下划线组成
# 123ok               不合法，不能由数字开头
# _xiaoming           合法
# 姓名                合法
# None                不合法，None为系统保留字
# __sina163__         合法
# 初级
# 1.从控制台输入圆的半径，计算周长和面积
# r = float(input("请输入圆的半径："))
# if r<= 0:
#     print("不能小于等于0")
# else:
#     d = 2 * r * 3.14
#     s = r ** 2 * 3.14
#     print("圆的周长为:%.2f,圆的面积为：%.2f" % (d, s))

# 2.一辆汽车以40km/h的速度行驶,行驶了45678.9km,求所用的时间
# v = 40
# s = 45678.9
# t = s / v
# print("所用时间为：%.2f h" % t)

# 3.华氏温度转摄氏温度【提示：将华氏温度转换为摄氏温度   F = 1.8C + 32】
# F = int(input("请输入华氏温度："))
# C = (F - 32) / 1.8
# print("华氏温度：%d 等于 摄氏温度：%d" % (F, C))

# 4.从控制台输入两个数，输出较大的值
# num1 = int(input("第一个数："))
# num2 = int(input("第二个数："))
# if num1 < num2:
#     print("较大的数为:%d" % num2)
# else:
#     print("较大的数为:%d" % num1)

# 中级
import random
# 1. x 为 0-99 中一个随机数,y 取 0-199 中间一个随机数,如果 x>y 则输出 x， 如果 x 等于 y 则输出 x+y，否则输出y
# x = random.randint(0, 99)
# y = random.randint(0, 199)
# if x > y:
#     print("x = %d" % x)
# elif x == y:
#     print("x + y = %d" % (x + y))
# else:
#     print("y = %d" % y)

# 2. 从控制台输入三个数，求这三个数的： 平均值、最大值、最小值、和(不允许使用max和min)
# num1 = int(input("第一个数："))
# num2 = int(input("第二个数："))
# num3 = int(input("第三个数："))
# mean = (num1 + num2 + num3) / 3
# print("平均值为：%d" % mean)
# max = num1
# if max < num2:
#     max = num2
# elif num2 < num3:
#     max = num3
# print("最大值为：%d" % max)
# min = num1
# if min > num2:
#     min = num2
# elif num2 > num3:
#     min = num3
# print("最小值为：%d" % min)
# sum = num1 + num2 + num3
# print("和为：%d" % sum)

# 3.从控制台输入三个数，把这三个数按照从小到大的顺序输出
# num1 = int(input("第一个数："))
# num2 = int(input("第二个数："))
# num3 = int(input("第三个数："))
# if num1 < num2:
#     num1, num2 = num2, num1
# if num1 < num3:
#     num1, num3 = num3, num1
# if num2 < num3:
#     num2, num3 = num3, num2
# print(num3, num2, num1)

# 4.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
# num = int(input("请输入一个三位数："))
# a = num % 10
# b = num // 10 % 10
# c = num // 100
# if a ** 3 + b ** 3 + c ** 3 == num:
#     print("是水仙花数！")
# else:
#     print("不是水仙花数！")







