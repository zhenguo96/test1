# 1.写一个函数，传入一个字符串时间：例如5点30分29秒表示为：’5:30:29’；然后返回下一秒的时间（字符串）
time1 = '23:59:59'
def add_time(time):
    list1 = [int(x) for x in time.strip().split(':')]
    # 计算总秒数
    seconds = list1[0] * 3600 + list1[1] * 60 + list1[2] + 1
    # 秒数
    list1[2] = seconds % 60
    # 分钟
    list1[1] = seconds % 3600 // 60
    # 小时
    list1[0] = seconds // 3600 % 24
    return ':'.join([str(x) for x in list1])
print(add_time(time1))






