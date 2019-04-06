# 从键盘上输入学生成绩，直到输入负数结束，求平均值
# sum1 = 0
# i = 0
# 非计数循环：循环次数不确定，根据条件退出
# while True:
#     grade = float(input("请输入成绩："))
#     if grade < 0:
#         break
#     sum1 += grade
#     i += 1
# print("平均成绩为：%.2f" % (sum1 / i))

# 剪刀、石头、布
import random
while 1:
    computer = random.randint(1,3)
    user = int(input("请输入剪刀、石头、布："))
    if user < 0 or user > 2:
        print("输入错误")
        continue # 终止当前这一次循环，重新判断条件，开启下一次循环
    result = user - computer
    if result == -2 or result == 1:
        print("你赢了，你出的是%d,电脑出的是%d" % (user, computer))
        break
    elif result == -1 or result == 2:
        print("你输了，你出的是%d,电脑出的是%d" % (user, computer))
        break
    else:
        print("和，你出的是%d,电脑出的是%d" % (user, computer))







