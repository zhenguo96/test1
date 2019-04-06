# 5.一个班有40个学生，请输入学生的期中考试成绩，成绩包括数学、英语、计算机。
n = 0
all = []
while n < 4:
    a = []
    shuxue = int(input("数学成绩："))
    yingyu = int(input("英语成绩："))
    jisuanji = int(input("计算机成绩："))
    a.append(shuxue)
    a.append(yingyu)
    a.append(jisuanji)
    all.append(a)
    n += 1
print(all)



