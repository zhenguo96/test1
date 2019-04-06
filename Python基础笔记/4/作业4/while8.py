'''
8.输出摄氏温度---华氏温度对照表，摄氏温度从0~100，每隔5度显示一个值。
提示：C＝5/9（F－32），C表示摄氏温度，F表示华氏温度
摄氏温度	华氏温度
0			32
5			41
10			50
15			59
'''
C = 0
listC = []
listF = []
while C <= 100:
    F = C * 1.8 + 32
    listF.append(int(F))
    listC.append(C)
    C += 5
print(listC)
print(listF)
print("摄氏温度    华氏温度")
for i in range(len(listC)):
    print(listC[i] , "           " , listF[i])



