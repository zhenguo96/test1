# 算数运算符
# + - * /   // (整除)  %（模运算）  **（幂运算）
a = 10
b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# 整除//
# 如果两个操作数都是整数，结果是整数
print(a // b)
# 如果有一个操作数都是浮点数，结果是浮点数
print(3.1 // b)

# % 模运算
# 两个数相除商是整数，取余数
a = 7
b = 2
print(a % b)

# 如果操作数是负数
# 计算结果的符号取决于第二个操作数
# r = a % b = a - n * b   n是小于a/b的最大整数
print(-5 % 2)
# 8/-5 = -1.6 找出比-1.6小的最大整数
print(5 % -2)
# 实例：
0# 判断变量的奇偶
#

# 获取整数的每一位数字
# a = int(input())
# # 个位数
# a % 10
# # 十位数
# a // 10 % 10
# # 百位
# a // 100
print(-5 // 3)# -5/3 = -1.6取小于-1.6的最大整数
# 判断整除
if a % 5 == 0:
    print("yes")
else:
    print("no")

# 幂运算
print(2 ** 3)
print(pow(2,3))

# 优先级
# ** > * / // % > + -

# 系统内置函数
# a = -4
# print(abs(a))    # 求绝对值
# a = 3.1634
# print(round(a,1))   # 四舍五入
# a = max(11,34,123,4312,32,235)
# print(a)

# math 库
import math
print(math.sqrt(2))      # 平方根
print(math.ceil(3.12))   # 上取整
print(math.floor(3.12))  # 下取整








