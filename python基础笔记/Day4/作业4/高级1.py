# 1. 将一元人民币兑换为1分、2分、5分的硬币有多少种兑换方案。
one = 0
sum1 = 0
while one <= 100:
    two = 0
    while two <= 50:
        five = 0
        while five <= 20:
            if one * 1 + two * 2 + five * 5 == 100:
                sum1 += 1
                print("1分%d张,2分%d张,5分%d张" % (one, two, five))
            five += 1
        two += 1
    one += 1
print(sum1)










