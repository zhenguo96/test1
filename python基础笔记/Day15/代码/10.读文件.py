# 读文件
# 1 打开文件
fp = open("f2.txt")

# 2 读内容
# data = fp.read()    # 读取文件所有内容
# data = fp.read(5)
# print(data)

# 读取一行
# data = fp.readline()
# while 1:
#     data = fp.readline().strip()
#     print(data)
#     if not data:
#         break

# 参数是字符数，如果字符数小于这一行的总字符数，则读入指定字符数，否则读取一行
# data = fp.readline(10)

# data = fp.readlines()
# data = [line.strip() for line in data]
# print(data)

# 文件遍历
# 文件指针是可迭代对象
for line in fp:
    print(line.strip())


# 3 关闭文件
fp.close()



a = [[1,4],[3,2],[2,3]]




