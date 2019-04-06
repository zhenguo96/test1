# 10. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下：
# a.将a字符串的数字取出，并输出成一个新的字符串
#   b.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
# c.输出a字符串出现频率最高的字母
# d.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False
a = "aAsmr3idd4bgs7Dlsf9eAF"
la = list(a)
b = ""
for i in range(len(a)):
    if str(la[i]).isdigit() == True:
        b += str(la[i])
print(b)

c = a.lower()
dict1 = {}
for j in range(len(c)):
    if c[j].isalpha():
        dict1[c[j]] = c.count(c[j])
print(dict1)

dict2 = {}
for k in range(len(a)):
    if c[k].isalpha():
        dict2[a[k]] = a.count(a[k])
print(max(dict2,key=dict2.get))


if "b" in a and "o" in a and "y" in a:
    print(True)
else:
    print(False)




