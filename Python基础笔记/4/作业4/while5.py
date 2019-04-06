# 5.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数
a = 1
b = []
while a < 100:
    if a % 7 == 0 and a % 3 != 0:
        b.append(a)
    if a % 3 == 0 and a % 7 != 0:
        b.append(a)
    a += 1
print(len(b))














