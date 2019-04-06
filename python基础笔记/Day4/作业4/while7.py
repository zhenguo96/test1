# 7.计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
a = 1
b = []
c = 0
while a < 1000:
    if a % 3 == 0 and a % 5 == 0 and a % 7 == 0:
        b.append(a)
    a += 1
print(b)
for i in range(len(b)):
    c += b[i]
print(c)








