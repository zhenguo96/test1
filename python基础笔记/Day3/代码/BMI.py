# BMI = 体重（公斤）/身高的平方（米）
# 单分支
"""
if 条件：
    【语句】
【后续语句】
执行逻辑：如果条件为真，则执行【语句块】，否则直接执行【后续语句】
"""
# 缺点：
# 代码比较长
# 无论满足不满足条件都要执行，效率较低
height = float(input("身高（米）："))
weight = float(input("体重（公斤）："))
bmi = weight / height ** 2
print(bmi)
# if bmi < 18.5:
#     print("吃吧")
# if 18.5 <= bmi < 23.9:
#     print("正好")
# if 23.9 <= bmi < 27:
#     print("偏胖")
# if bmi >= 27:
#     print("肥胖")

# 双分支语句
'''
if 条件:
    【语句A】
else:
    【语句B】
执行逻辑:如果条件为真，则执行【语句A】，否则执行【语句B】
'''
# if bmi < 18.5:
#     print("瘦子")
# else:
#     if bmi < 23.9:
#         print("健康")
#     else:
#         if bmi < 27:
#             print("该减肥了")
#         else:
#             print("胖的不行")

# 多分支语句
'''
if 条件1:
    【语句1】
elif 条件2:
    【语句2】
elif 条件3:
    【语句3】
...
elif 条件n:
    【语句n】
else:
    【语句】
执行逻辑：首先判断条件1，如果为真，则执行语句块1，如果为假，则继续判断条件2，条件2为真，执行语句2，如果为假以此类推，如果都不满足，执行else
'''

if bmi < 18.5:
    print("一道闪电")
elif bmi < 23.9:
    print("棒")
elif bmi < 27:
    print("有的救")
else:
    print("放弃治疗")









