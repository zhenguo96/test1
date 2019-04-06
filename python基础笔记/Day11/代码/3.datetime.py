import datetime
from datetime import datetime

# datetime对象
d1 = datetime.now()
# print(d1,type(d1))

# 年月日、时分秒
print(d1.year,d1.month,d1.day,d1.hour,d1.minute,d1.second)
# 判断闰年
date = d1.date()
print(date,type(date))

# 转时间字符串
d2 = d1.isoformat()
print(d2,type(d2))

# 自定义时间格式
d3 = d1.strftime("%Y-%m-%d")
print(d3)

# 计算差值
d4 = datetime(2019,2,28,12,32,21)
d5 = datetime(2019,3,10)
d6 = d5-d4
print(d6)














