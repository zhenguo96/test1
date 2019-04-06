# 创建元组
t1 = (1,2,3,4)
t1 = (1,)   # 元组只有一个元素的话，必须带逗号
t1 = ()     # 空元组
t1 = tuple()# 空元组
t1 = tuple("hello")
t1 = tuple([10,20,30])
print(t1,type(t1))

# 访问元组的元素
print(t1[1], t1[-2])
# print(t1[3])  # 越界会报错
# t1[0] = 11      # 元素不可变

# 通用操作
t1 = (1,2,3)
t2 = (4,5,6)
# + 拼接，产生新元组
print(t1 + t2)
# * 重复
# print(t1 * 2)

# 切片
# t1 = t1 + t2
# print(t1[::-1])
# print(t1[5:-5:-1])
# print(t1[1::2])

# 成员运算符 in
# print(5 in t1)
#
# # 元素个数，元组长度
# print(len(t1))
#
# # 统计函数
# print(max(t1), min(t1), sum(t1))

# 元素查找
# print(t1.index(2))
# # print(t1.index(55))# 元素不存在报错
# print(t1.count(1))

# 遍历
for index in range(len(t1)):
    print(t1[index])
    t1 = ((1,2,3),(4,5,6))
    for i in range(len(t1)):
        print(t1[index][i],end=' ')

