# os模块文件和目录操作
import os
# print(os.name)      # 操作系统名字
# print(os.environ)   # 操作系统环境变量path

# 目录操作
'''
. 当前目录
.. 表示上级目录
./ 1

## 绝对路径：c:
'''
# print(os.curdir)    # 当前目录，相对目录
# print(os.getcwd())  # 当前目录绝对路径
# # 以列表的形式返回当前目录下的对象（文件和子文、目录）
# print(os.listdir())
# 创建目录和删除目录
# os.mkdir('./1/2')
# os.rmdir("./1")
# 修改文件或者文件夹的名称
# os.rename('回顾.py','回顾1.py')

# 执行系统命令，和你在cmd下执行的命令一致
# os.system('dir')
# import time
# for i in range(70):
#     print(" "*i,end='')
#     print(("----------->"))
#     time.sleep(0.01)
#     os.system('cls')

# 目录遍历
# walk递归遍历指定目录及其子目录
# for path, a, file in os.walk(r'E:\千锋课堂资料\Day16\代码'):
#     print(path)
#     print(a)
#     print(file)

# 路径处理
# 路径拼接
# print(os.path.join(os.getcwd(),"helloworld.txt"))

# 获取路径的路径名
# print(os.path.dirname(r'E:\千锋课堂资料\Day16\代码\3.os.txt'))
# 获取父路径
# print(os.path.dirname(os.path.dirname(r'E:\千锋课堂资料\Day16\代码\3.os.txt')))

# 文件是否存在
# print(os.path.exists(r'E:\千锋课堂资料\Day16\代码\2.txt'))

# 获取文件的后缀名
# print(os.path.splitext(r'E:\千锋课堂资料\Day16\代码\2.txt'))````````````````````````````````````````````````````````


# d = {'name':'tom', 'age':18}
# def a(*args):
#     print(args)
# a(*d)
#
# for i,j in enumerate(d):
#     print(i,j)





















