import calendar
# 某月的万年历
print(calendar.month(2019,3))
# 以二维列表形式保存了万年历数据
print(calendar.monthcalendar(2019,3))

# 判断是否是闰年
print(calendar.isleap(2019))

# 某月的有效天数，第一天是星期几
print(calendar.monthrange(2019,3))








