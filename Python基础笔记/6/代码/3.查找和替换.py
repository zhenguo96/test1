# str1 = 'a fox jumped over the fence'
# count 子串出现的次数
# count(sub, start=0, end=len(str))
# print(str1.count('e',10,16))

# find(sub, start=0, end=len(star))
# 从左向右查找给定子串，如果找到返回子串第一个字符的下标，找不到返回-1
# print(str1.find("fox"))   # 2
# print(str1.find('1fox'))  # -1
# print(str1.find("fox", 3))
# # rfind
str1 = 'a fox jumped over fox the fence'
# print(str1.rfind("fox"))
# print(str1.rfind("fox",))
#
# # replace(old, new, [count]) 返回新串
res = str1.replace("fox", "tiger", 1) # 只替换一个
print(res)
print(str1)
