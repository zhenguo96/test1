# 4. 写函数，计算并返回传入字符串中数字个数、字母个数、空格个数以及其他字符的个数。
str1 = "my name is sunck, i am 18 years old."
def func1(s):
    ls = list(s)
    num1 = 0
    s1 = 0
    k1 = 0
    zf = 0
    for i in range(len(ls)):
        if ls[i].isdigit():
            num1 += 1
        elif ls[i].isalpha():
            s1 += 1
        elif ls[i] == ' ':
            k1 += 1
        else:
            zf += 1
    return num1,s1,k1,zf
res = func1(str1)
print(res)










