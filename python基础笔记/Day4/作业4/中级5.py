'''
5.猜数字
从键盘上输入一个整数，如果等于你规定的整数，就猜中了，如果小于规定的数，提示“小了”，否则提示“大了”，直到猜中位置
'''
import random
num1 = random.randint(0,100)
while True:
    num2 = int(input("请输入一个整数："))
    if num2 < num1:
        print("小了")
    elif num2 > num1:
        print("大了")
    else:
        print("猜对了")
        quit()




