# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# day = int(input("请输入日期："))
# days = 0
# month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if year > 0 and 0 < month < 13 and 0 < day < 32:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         month_day[1] = 29
#         if month == 2 and day > 29:
#             print("错误的日期输入")
#         elif month == 4 or month == 6 or month == 9 or month == 10 and day > 30:
#             print("错误的日期输入")
#         else:
#             for m in range(month - 1):
#                 days += month_day[m]
#             print(days + day)
#     else:
#         if month == 2 and day > 28:
#             print("错误的日期输入")
#         elif month == 4 or month == 6 or month == 9 or month == 10 and day > 30:
#             print("错误的日期输入")
#         else:
#             for m in range(month - 1):
#                 days += month_day[m]
#             print(days + day)
# else:
#     print("错误的日期输入")



year = int(input("请输入年分："))
month = int(input("请输入月份："))
day = int(input("请输入日："))
print("-" * 20)
day += (month - 1) * 30     # 一个月按30天计算 然后day = 月份减少1,乘以30  +  加上天数
print(day)
if month < 9:       # 如果月份小于9
    day += month // 2   # 月   day = day + month // 2
else:
    day += (month + 1) // 2
if month > 2:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        day -= 1
    else:
        day -= 2
print("是%d年的第%d天" % (year,day))









