'''
3.五位数中，对称的数称为回文数，打印所有的回文数并计算个数
12321
'''
num = 10000
index = 0
while num < 100000:
    num5 = num % 10
    num4 = num // 1000 % 10
    num3 = num // 100 % 10
    num2 = num // 10 % 10
    num1 = num // 10000
    if num5 == num1 and num2 == num4:
        print(num)
        index += 1
    num += 1
print("五位数里回文数个数有%d个" % index)






