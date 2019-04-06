import time
t1 = time.time()
print(t1)

# 得到时间元组
t2 = time.gmtime(t1)        #utc
t3 = time.localtime(t1)     #本地时间
print(t2)
print(t3)

# 时间字符串
# %Y 年份 %m 月份 %d 天
# %H 小时 %M 分钟 %S 秒
t4 = time.strftime("%Y-%m-%d",t3)
print(t4,type(t4))

# 日期字符串转时间元组
t5 = time.strptime("2019-03-10 10:28:31","%Y-%m-%d %H:%M:%S")
print(t5)

# 时间元组转时间戳
t6 = time.mktime(t5)
print(t6)

# 日期差值
diff = int(t1 - t6)
print(diff)
print(diff // (3600 * 24))  # 天
print(diff % (24*3600) // 3600)     # 小时
print(diff % 3600 // 60)      # 分钟
print(diff % 60)    # 秒数

# sleep 暂停程序的执行
# print("start")
# time.sleep(5)
# print("end")

# 测试程序或函数的执行时间
start = time.time()
for i in range(10):
    a = 1 + 2
end  = time.time()
print(end-start)











