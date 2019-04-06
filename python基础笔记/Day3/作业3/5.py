'''
5. 任给两个实数，判断这两个实数作为坐标所在的象限。
例如给2.5 -5.6  显示在第4象限！
提示: 考虑在坐标轴上和原点的情况
'''
x = float(input("请输入x轴坐标："))
y = float(input("请输入y轴坐标："))
if x == y == 0:
    print("该坐标在坐标原点")
elif x == 0 and y != 0:
    print("该坐标在y轴上")
elif y == 0 and x != 0:
    print("该坐标在x轴上")
elif x > 0 and y > 0:
    print("该坐标在第一象限")
elif x < 0 and y > 0:
    print("该坐标在第二象限")
elif x < 0 and y < 0:
    print("该坐标在第三象限")
elif x > 0 and y < 0:
    print("该坐标在第四象限")







