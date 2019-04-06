# 5.定义列表，存放10个学生的成绩【成绩值0-100】，获得成绩之和，平均成绩，最小成绩，最大成绩。
score = [99, 84, 75, 95, 96, 84, 88, 79, 91, 90]
sum1 = 0
min1 = score[0]
max1 = score[0]
for i in range(len(score)):
    sum1 += score[i]
    if min1 > score[i]:
        min1 = score[i]
    if max1 < score[i]:
        max1 = score[i]
    mean1 = sum1 / len(score)
print("成绩之和：%d，平均成绩：%d，最小成绩：%d，最大成绩：%d" % (sum1, mean1, min1, max1))





