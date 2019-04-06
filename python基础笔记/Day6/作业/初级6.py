# 6.任给一个字符串，请验证是否是手机号，手机号为11位数字，开头三位必须是130,151,186
# num1 = list(input("请输入11位手机号："))
num1 = list(input("请输入11位手机号码："))
i = 0
a = int(''.join(num1[0]+num1[1]+num1[2]))
while i < len(num1):
    i += 1
    if a == 130 or a == 151 or a == 186:
        continue
    else:
        print("开头三位必须是130，151，186")
        quit()
if i != 11:
    print("手机号码位数不对")
else:
    print(''.join(num1))








