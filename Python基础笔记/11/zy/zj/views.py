dictstu = []
def shuru():
    for i in range(2):
        students = input("输入第%d个学生的信息：" % (i+1))
        d = students.split("    ")
        sum1 = int(d[2]) + int(d[3])
        mean1 = sum1 // 2
        d.append(str(sum1))
        d.append(str(mean1))
        dictstu.append(d)
    return 0

def shuchu():
    print("姓名             学号          数学成绩     计算机成绩        总成绩       平均成绩")
    for i in range(len(dictstu)):
        print("            ".join(dictstu[i]))
    return 0

def chazhao():
    p = input("请输入要查找的学号：")
    print("姓名             学号          数学成绩     计算机成绩        总成绩       平均成绩")
    for i in range(len(dictstu)):
        if p == dictstu[i][1]:
            print("            ".join(dictstu[i]))
    return 0

def paixu():
    print("姓名             学号          数学成绩     计算机成绩        总成绩       平均成绩")
    for i in range(len(dictstu)):
        for j in range(i,len(dictstu)):
            if dictstu[i][4] < dictstu[j][4]:
                dictstu[i], dictstu[j] = dictstu[j],dictstu[i]
    for k in range(len(dictstu)):
        print("            ".join(dictstu[k]))
    return 0











