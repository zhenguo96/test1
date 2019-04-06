'''
7.python1902班有10个同学，请你设计一个程序输入每个同学的测验成绩，请总成绩和平均成绩
'''
student = 1
rsum = 0
while student <= 10:
    results = int(input("请输入第%d个同学的成绩：" % student))
    rsum += results
    student +=1
mean = rsum / (student - 1)
print("python1902班的%d个同学，总成绩为：%d,平均成绩为：%d" % (student - 1, rsum, mean))








