# 逻辑运算符：构造复杂条件
# 逻辑与 and 并且同时
import random
# a = random.randint(1,5)
# if a > 1 and a < 3:
#     print("true")
# else:
#     print("false")
# 可以转换为假： ''  0  0.0  False  None
# 如果第一个操作数是真，结果就是第二个操作数的值
print(11 and "ok")
# 如果第一个操作数是假，结果就是第一个操作数的值
print(0 and 15)
# 如果第一个操作数为假，逻辑与不计算第二个操作数的值，这个叫逻辑短路
a = 3
a > 3 and exit()
print("asdasd")

# 逻辑或 or
# 如果第一个操作数为真，结果就是第一个操作数
print('ok' or 15)
# 如果第一个操作数为假，结果就是第二个操作数的值
print(0 or 10)

# 如果逻辑或的第一个操作数为真，不计算第二个操作数，这也是逻辑短路
1 or print("****")

# 逻辑非 not 逻辑取反，如果原来是真，结果就是False，否则结果就是True
print(not 10)   # False
print(not '')   # True

# 判断闰年：能被4整除，不能被100整除，或者能被400整除的
year = random.randint(1970, 2019)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("%d年是闰年" % year)
else:
    print("%d年不是闰年" % year)

