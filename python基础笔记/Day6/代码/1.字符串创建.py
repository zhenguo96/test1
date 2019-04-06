# str
# 空串
# s1 = ''
# s2 = str()
# # print(type(s1), type(s2))
# s3 = str([1,2])
# print(s3,type(s3))
# s4 = eval(s3)   # 字符串转列表
# print(s4, type(s4))

# 获取子串
s1 = "123456789123456789123456789"
print(s1[0], s1[-len(s1)])
# s1[0] = "hello" # 不支持修改
s2 = "hello" + s1[9:12]
print(s1)
print(s2)

# 原生字符
# path = "C:\\bj1902\\note\\6_字符串、元组、字典\\doc"
# 原生字符串，反斜线不在代表转义
# path = r"C:\bj1902\note\6_字符串、元组、字典\doc"
# print(path)
