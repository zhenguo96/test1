# 1.3000米长的绳子，每天减一半，问多少天这个绳子会小于5米？不考虑小数
day = 0
l = 3000
while l >= 5:
    l /= 2
    day += 1
print("%d天后绳子小于5米" % day)







