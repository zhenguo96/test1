# 模拟骰子
# 第一生成一个[1,6]的随机数
# 根据随机数判断吃啥
import random
suiji = random.randint(1,6)
# if-elif方法
# if suiji == 1:
#     print("吃1")
# elif suiji == 2:
#     print("吃2")
# elif suiji == 3:
#     print("吃3")
# elif suiji == 4:
#     print("吃4")
# elif suiji == 5:
#     print("吃5")
# elif suiji == 6:
#     print("吃6")

# if 方法
# if suiji == 1:
#     print("吃1")
# if suiji == 2:
#     print("吃2")
# if suiji == 3:
#     print("吃3")
# if suiji == 4:
#     print("吃4")
# if suiji == 5:
#     print("吃5")
# if suiji == 6:
#     print("吃6")

# if-else 方法
if suiji == 1:
    print("炸蝎子")
else:
    if suiji == 2:
        print("炸蚕蛹")
    else:
        if suiji == 3:
            print("炸蜘蛛")
        else:
            if suiji == 4:
                print("吃点啥")
            else:
                if suiji == 5:
                    print("炸蚂蚱")
                else:
                    if suiji == 6:
                        print("不吃了")





