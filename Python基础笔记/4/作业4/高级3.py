# 3.任给一个正整数，输出这个数是几位数，并将该整数逆序输出
num1 = int(input("请输入一个正整数："))
index = 0
list1 = list(str(num1))
while 1:
    num1 //= 10
    if num1 == 0:
        break
    index += 1
list2 = list1[::-1]
print(index + 1)
print("".join(list2))












