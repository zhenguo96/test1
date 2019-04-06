# 3.传入不定个数的字符串拼接第一个和最后一个字符串
str1 = input("请输入不定个数的字符串：")
def pinjie(s):
    str2 = ""
    str2 += s[0] + s[-1]
    return str2
res = pinjie(str1)
print(res)







