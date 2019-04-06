# 2. 输入一个字符串，自己统计该字符串有多少个字符，不允许用len函数
str1 = input("输入一个字符串：")
i = 1
while 1:
    str2 = str1[:i]
    if str2 == str1:
        break
    i += 1
print(i)















