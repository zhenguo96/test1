# 3.计算从1到100以内所有3的倍数的和
a = 1
b = []
c = 0
while a < 100:
    if a % 3 == 0:
        b.append(a)
    a += 1
print(b)
for i in range(len(b)):
    c += b[i]
print(c)








