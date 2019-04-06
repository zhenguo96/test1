# 读文件
# 1.打开文件
fp = open('f2.txt','w')

# 2 写字符串到文件
# 可以把字符串写入文件
# fp.write("鲲之大，一锅炖不下，")
a = ['hello\n','world\n','welcome to beijing\n','毒死\n']
# 把字符串列表写入文件
fp.writelines(a)
# 3.关闭文件
fp.close()









