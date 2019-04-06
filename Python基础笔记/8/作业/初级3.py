# 3.	传入一个正整数，判断这个数是否是素数，如果是返回True，否则返回False
num1 = int(input("输入一个正整数："))
def sushu(num1):
    for i in range(2,int(num1 ** 0.5)):
        if num1 % i == 0:
            return False
    return True
res = sushu(num1)
print(res)







