# 2.求1--100之间可以被7整除的数的个数
a = 0
b = []
while a < 100:
    if a % 7 == 0:
        b.append(a)
    a += 1
print(len(b))







