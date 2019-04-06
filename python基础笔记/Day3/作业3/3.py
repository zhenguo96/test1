# 3.输入三角形的三边，输出是那种三角形（普通三角形、等腰三角形、等边三角形、直角三角形、等腰直角三角形）。提示：要判断是否构成三角形
num1 = float(input("第一条边长："))
num2 = float(input("第二条边长："))
num3 = float(input("第三条边长："))
if num1 < num2:
    num1, num2 = num2, num1
if num1 < num3:
    num1, num3 = num3, num1
if num2 < num3:
    num2, num3 = num3, num2
if num3 + num2 > num1:
    # 实数不能直接判等和不等，abs(a - b)<1e-7
    if num1 == num2 == num3:
        print("构成等边三角形")
    elif num1 ** 2 == num2 ** 2 + num3 ** 2 and num2 == num3:
        print("构成等腰直角三角形")
    elif num1 ** 2 == num2 ** 2 + num3 ** 2:
        print("构成直角三角形")
    elif num1 == num2 or num1 == num3 or num3 == num2:
        print("构成等腰三角形")
    else:
        print("构成普通三角形")
else:
    print("不能构成三角形")




