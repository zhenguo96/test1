# 集合
s1 = set()
#　自动去重
s2 = {1,21,3,4,True,3,12}
print(s2)
# add
s1.add(10)
s1.add((1,2))
s1.add('hello')
print(s1)

# 合并
s1.update(s2)
print(s1)

# 删除元素
s1.remove("hello")
print(s1)

# 随机删除一个元素
# s1.pop()
# print(s1)

# discard
s1.discard(110)     # 元素不存在不会报错
s1.remove(4)        # 元素不存在会报错

# 并、交、差
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# 两个集合并：新集合包所有的元素
res = s1 | s2
print(res)
# 交集：新集合包含了两个集合共有的元素
res = s1 & s2
print(res)
# 差集：新集合由属于第一个集合的元素除去第一个集合和第二个集合的共有元素
res = s2 - s1
print(res)

s1 = "helloowooweioei"
print(set(s1))




