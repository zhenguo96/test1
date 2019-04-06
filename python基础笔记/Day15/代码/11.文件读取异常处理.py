# try:
#     fp = open('f2.txt')
#     fp.write("*********************")
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# finally:
#     print("finally")
#     fp.close()
# 上下文管理 只要文件打开了，系统就一定会关闭它
# with open('f2.txt') as fp:
#     fp.write("11111")

# 上下文管理在类中的实现
class FileOperate:
    def __init__(self,fileName,mode='r'):
        self.fileName = fileName
        self.mode = mode
    def __enter__(self):
        print("打开文件")
        self.fp = open(self.fileName,self.mode)
        return self.fp
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        self.fp.close()
with FileOperate('f2.txt') as fp:
    data = fp.read()
    print(data)






