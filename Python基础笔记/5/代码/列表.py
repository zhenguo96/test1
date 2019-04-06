a = [1,2,3]
b = [2,3,4]
# 列表的拼接：将两个列表合并为一个新列表
# res = a + b
# print(res)
# print(a)
# print(b)
# 元素重复，产生新列表
# res = a * 3
# print(res)
# print(a)

# 成员判断 in 如果元素在列表中返回True，否则返回False
# not in 如果元素不在列表中返回Fal，否则返回True
# print(2 in a)
# print(12 not in a)

# 切片:取出一个子列表
# list[start:end:step]
# start：起始下标，默认是0
# end：结束下标，默认是列表长度，但是不包含end所指的元素
# step：步长，默认是1，正数代表从左向右切，负数代表从右向左切，绝对不能是0
#                 1 代表从start所指元素开始依次取所有元素，到end之前
a = [1,2,3,4,5,6,7,8,9]
# 从左向右切
# print(a[:5])
# print(a[:5:2])  # 隔一个取一个
# print(a[:])     # end默认是列表长度，只要end大于最大下标，就从start取到末尾
# print(a[:100])
# 从左向右取，end下标无论正负，必须在start下标右边
# print(a[-9:-1])   # [1,2,3,4,5,6,7,8]
# print(a[-9:5])
# print(a[5:-9])
# print(a[5:-1])
# 从右向左取
# start 默认-1 end 默认是-len(a)-1
# print(a[-1:-5:-1])
# print(a[::-1])    # 取所有元素，反向列表
# print(a[-1::-1])
# print(a[:-100:-1])
# 从右向左取，end所指元素必须在start所指元素的左边， step必须是负数
# print(a[5:-9:-1])
# print(a[-3:2:-1])
# print(a[3:-1:-1])

# len 获取元素个数
print(len(a))
# 统计函数
print(max(a), min(a), sum(a))
print(sum(a[:7]))