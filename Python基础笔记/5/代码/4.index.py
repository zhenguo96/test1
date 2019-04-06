# 元素的查找
# index(value, [start], [end])
# 从左向右查，找到第一个满足条件的元素
# 返回值：如果元素存在，返回其下标，否则报valueError
# print(a.index(31))
# if 46 in a:
#     print(a.index(46))
# 从下标为3的元素开始向右查找值等于31的元素
# print(a.index(31, 3))
a = [10, 22, 31, 89, 31, 76, 45]
# 获取31元素的个数
count = a.count(31)
# 保存所有值等于31的元素的下标
temp = []
# 起始下标
start = 0
while count:
    # 找到值等于31的元素的下标添加到列表temp中
    temp.append(a.index(31, start))
    count -= 1
    start = temp[-1] + 1
print(temp)

# count 获取列表中值等于给定数据的元素个数
# print(a.count(31))
# 元素不存在，返回0
# print(a.count(331))



