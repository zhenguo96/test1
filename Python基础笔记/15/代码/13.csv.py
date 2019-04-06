import csv

# # 读文件
# with open("csv/bank.csv") as fp:
#     # 获取csv操作对象
#     # 参数：fp 文件指针
#     # dalimiter 分隔符，如果是逗号，可以省略
#     reader = csv.reader(fp,delimiter=':')
#     for line in reader:
#         print([int(x) if x.isdigit() else x for x in line])

# 写csv文件
a = {'a':10,'b':[1,2,3]}
# newline 换行符，默认是\n，如果设置为空字符串，则文件中的空行会被去掉
with open("csv/dict.csv",mode="w",newline='') as fp:
    # csv写对象
    writer = csv.writer(fp)
    for key in a:
        # writerow写入的是可迭代对象
        writer.writerow(a[key])







