# 4.B哥去参加青年歌手大奖赛,有10个评委打分，去掉一个最高一个最低，求平均分
list1 = [99, 98, 91, 93, 92, 97 ,94, 96, 95, 90]
max1 = list1[0]
min1 = list1[0]
sum1 = 0
for i in range(len(list1)):
    if max1 < list1[i]:
        max1 = list1[i]
    if min1 > list1[i]:
        min1 = list1[i]
for j in range(len(list1)):
    if list1[j] == max1:
        list1[j] = 0
    if list1[j] == min1:
        list1[j] = 0
for k in range(len(list1)):
    sum1 += list1[k]
mean = sum1 / (len(list1) - 2)
print(mean)





