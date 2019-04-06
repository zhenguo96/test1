from collections import deque
import os
import os.path
class Traverse:
    def __init__(self,path):
        self.path = path
        self.queue = deque()    # 使用双端队列模拟栈、队列4

    # 1.walk
    def traverse_by_walk(self,func):
        """
        :param func: 必须传入一个函数，完成自己的操作
        :return: 
        """
        for path,chile_dir,files in os.walk(self.path):
            func(path,chile_dir,files)

    def a(self,path,chile_dir,files):
        for file in files:
            print(file)

    def recurse_path(self,path):
        if not os.path.isdir(path):
            return
        items = os.listdir(path)
        for item in items:
            tem = os.path.join(path,item)
            if os.path.isdir(tem):
                self.recurse_path(tem)
            else:
                print(tem)

    def traverse_depth_first(self):
        #用双端队列模拟栈
        self.queue.append(self.path)
        while len(self.queue): #栈不为空
            # 栈顶元素出栈
            top = self.queue.pop()
            childDirs = os.listdir(top)
            for item in childDirs:
                tmp = os.path.join(top,item)  #绝对路径
                if os.path.isdir(tmp):  #是目录入栈
                    self.queue.append(tmp)
                else:
                    print(item)

tv = Traverse(r'E:\千锋课堂资料\Day16\代码')
# tv.recurse_path(r'E:\千锋课堂资料\Day16\代码')
tv.traverse_depth_first()
# tv.traverse_by_walk(tv.a)

# tv.traverse_by_walk(lambda a,b,c:print(a,b,c))





















