# 6.求1--n之间可以被7整除的数的个数，参数是n，返回个数
n = int(input("n是多少："))
def count1(n):
    index1 = 0
    for i in range(1,n+1):
        if i % 7 == 0:
            index1 += 1
    return index1
res = count1(n)
print(res)






