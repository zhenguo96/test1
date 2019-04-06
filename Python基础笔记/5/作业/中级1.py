# 1.输入某年某月某日，判断这一天是这一年的第几天
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入天数："))
days = 0
month1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(month1)):
    if year % 4 == 0 and year % 100 != 0 or year % 100 == 0:
        month1[2] = 29
    if i < month:
        days += month1[i]
days += day
print(days)



