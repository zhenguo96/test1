# 9任意输入一段文字，统计有多少个单词（用空格隔开）、多少个数字、多少字母、多少空格。
s = "my name is sunck i am 18 years old"
print("%d个单词" % len(s.split(" ")))
str1 = list(s)
kongge = str1.count(" ")
print("%d空格" % kongge)
num1 = 0
for i in range(len(str1)):
    if str(str1[i]).isdigit() == True:
        num1 += 1
print("%d个数字" % num1)
danci = len(str1) - num1 - kongge
print("%d个字母" % danci)



