# 文件定位
with open('f1.data') as fp:
    # 文件指针在文件开头
    print(fp.tell())    # 显示文件指针位置
    fp.seek(4,0)
    data = fp.read()
    print(data)











