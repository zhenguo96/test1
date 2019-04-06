import re
# findall 匹配所有满足要求的项
# print(re.findall(r'hello',"akshfkshelloasdhfklahelloalhdsaf;"))

# data = input("请输入数学、英语、计算机的成绩（以空格做分隔符）：")
# print(data)

# split
# print(re.split(r' +|1+',data))



# sub、subn替换
s1 = "kkkkkkk9923sdfdsffsf12111jlkljklj333"
print(re.sub(r'\d','0',s1))
print(re.subn(r'\d','0',s1,200))     # 替换后的字符串，替换次数


















