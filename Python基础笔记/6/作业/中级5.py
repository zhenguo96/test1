# 5.输入一个字符串，压缩字符串如下aabbbccccd变成a2b3c4d1
c = "aabbbccccd"
dict1 = {}
str1 = ""
for j in range(len(c)):
    if c[j].isalpha():
        dict1[c[j]] = c.count(c[j])
for key,value in dict1.items():
    a,b = (key,value)
    str1 += a + str(b)
print(str1)



