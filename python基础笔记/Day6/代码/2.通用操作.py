# 通用操作

# 字符串拼接，产生一个新的字符串
# res = s1 + s2
# print(res)
# 重复   产生新串
# print("*" * 50)
# print("-" * 50)
#
# # in    字串是否在指定串中
# print('asj' in s1)
# print('asd' in s1)
#
# #　切片
# print(s1[:5])
# print(s1[-len(s1):-len(s1)+5])
#
# # 反着切
# s1 = "abcdefghijklmns"
# s2 = "123456789"
# print(s1[::-1])

for num in range(10000, 100000):
    s1 = str(num)
    s2 = s1[::-1]
    print(s2)
    if s1 == s2:
        pass

