"""
while 条件：
    【代码块——循环体】
【后续代码】
执行流程：首先判断条件，如果条件为真，执行循环体，然后重新判断条件，如果成立，继续循环，直到条件不成立退出循环，执行后续代码
"""
# i = 0 # 循环变量赋初值
# while i < 100:  # 构造循环条件
#     print("hello world")
#     i += 1      # 修改循环变量的值，等到某一次执行后，让循环条件为假

# 1.计算 1+2+3+...+100
# i = 0
# sum1 = 0
# while i <= 100:
#     sum1 += i
#     i += 1
# print(sum1)

# 2.计算 2+4+6+8+...+100
# i = 0
# sum2 = 0
# while i <= 100:
#     sum2 += i
#     i += 2
# print(sum2)

# 3.计算100以内3的倍数的和
# i = 0
# sum1 = 0
# while i <= 100:
#     if i % 3 == 0:
#         sum1 += i
#     i += 1
# print(sum1)

# 4.计算 1 * 2 * 3 * 4 * ... * n,n从键盘上输入
num1 = int(input("求几的阶乘就输入几："))
i = 1
num2 = 1
while i <= num1:
    num2 *= i
    i += 1
print("%d的阶乘是%d" % (num1,num2))



