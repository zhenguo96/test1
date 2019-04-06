d1 = {"a":2,'b':5,'c':6}
# 通过键存取
# d1[key]
# print(d1['a'])
d1['a'] = 100
# print(d1)
# 如果键不存在，就是添加键值对
d1['ab'] = 98
# print(d1)

#　get(key,default)
# print(d1['f'])  # 如果键不存在会报错
# print(d1.get('f',10))
# http://www.baidu.com/?keyword=印巴战争&name=tom&age=1
# temp ="http://www.baidu.com/?keyword=印巴战争&name=tom&age=1".partition("?")
# print(temp[2])
# temp = temp[2].split('&')
# print(temp)
# d2 = {}
# for i in range(len(temp)):
#     key, value = temp[i].split("=")
#     d2[key] = value
# print(d2)
# # 如果指定键不存在，默认返回None，如果指定了第二个参数(默认值)，会返回默认值
# print(d2.get('sex', '男'))

# 删除键值对
# pop删除指定键，会返回键对应的值
# print(d1.pop('a'))
# print(d1)
# # 清空字典
# d1.clear()
# print(d1)
# # 将d3合并到d1中，如果键重复，d3中键值对会覆盖d1中对应的键值对
# d3 = {'n':100, 'm':90, 'a':20}
# res = d1.update(d3)
# print(d1)
# 通过key遍历
d1 = {"a":2,'b':5,'c':6}
for key in d1:
    print(key,'----',d1[key])
# 返回一个由所有值构成的"列表"
print(list(d1.values()))
for v in d1.values():
    print(v)

# keys
print(list(d1.keys()))

# 同时获取键和值
# print(list(d1.items()))
# for k, v in d1.items():
#     # 不能通过修改v修改键所对应的值
#     print(k,v)

# enumerate
# 获取下标和键
for index,key in enumerate(d1):
    print(index,key)

# in 只能判断某个键是否在字典中
print('a' in d1)
print('aaa' in d1)


