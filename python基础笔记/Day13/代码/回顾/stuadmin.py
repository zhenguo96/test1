from sutdents import *
class GradeManage:
    def __init__(self,num):
        self.num = num  # 学生人数
        self.grades = [] # 保存成绩
    def menu(self):
        while True:
            print("""******欢迎使用成绩管理系统********
                [1] 学生信息输入
                [2] 学生信息输出
                [3] 查找学生信息
                [4] 成绩排序
                [0] 退出
                ------------------------
            """)
            choice = int(input("请输入你的选择："))
            if choice == 0:
                print("欢迎下次再来！！")
                exit()
            elif choice == 1:
                self.input()
            elif choice == 2:
                self.outpu()
            elif choice == 3:
                sno = input("请输入要查找的学号：")
                student = self.find(sno)
                print(student)
            elif choice == 4:
                self.sort()
            else:
                print("没有该选择，请重新输入！")
    def input(self):
        for i in range(1,self.num +1):
            print("请输入第{}个学生信息：".format(i))
            pass

    def __get_data(self):
        info = input()
        info = [x for x in info.split(" ") if len(x) > 0]
        # info = [x for x in info x.isdigit() else x x for in info]
        return  info









