# 6.计算1到500以内能被7整除但不是偶数的数的个数
a = 1
b = []
while a < 500:
    if a % 7 == 0 and a % 2 != 0:
        b.append(a)
    a += 1
print(len(b))





