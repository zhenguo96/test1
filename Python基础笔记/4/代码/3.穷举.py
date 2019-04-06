# 韩信点兵：报数5，余2，报数7，余4，报数10，余7，最少多少人
# count = 0
# while 1:
#     count += 1
#     if count % 5 == 2 and count % 7 == 4 and count % 10 == 7:
#         print(count)
#         break

# 不定方程求解
# 2x + 3y = 100
# x>=0, y>=0
x = 0
while x <= 50:
    y = 0
    while y < 34:
        if 2 * x + 3 * y == 100:
            print(x, y)
        y += 1
    x += 1








