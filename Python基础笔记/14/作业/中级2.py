class Person():
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Workers(Person):
    def __init__(self,id,name,hour,sx):
        super().__init__(id,name)
        self.hour = hour
        self.sx = sx
        self.wage = int(self.hour) * int(self.sx)
    def __str__(self):
        return '{}{}{}'.format(self.id,self.name,self.wage)

class Sales(Person):
    def __init__(self,id,name,xse,tc):
        super().__init__(id,name)
        self.xse = xse
        self.tc = tc
        self.wage = self.xse * self.tc
    def __str__(self):
        return '{}{}{}'.format(self.id,self.name,self.wage)

class Manager(Person):
    def __init__(self,id,name,g):
        super().__init__(id, name)
        self.g = g
        self.wage = self.g
    def __str__(self):
        return '{}{}{}'.format(self.id,self.name,self.wage)

class SalesManager(Sales):
    def __init__(self,id,name,xse,tc,g):
        super().__init__(id, name,xse,tc)
        self.g = g
        self.wage = self.xse * self.tc + self.g
    def __str__(self):
        return '{}{}{}'.format(self.id,self.name,self.wage)

class ManageSystem():
    def __init__(self):
        self.workerslist = []

    def choice(self):
        while 1:
            print("""
                ******欢迎使用工资管理程序********
                [1] 工人信息输入
                [2] 销售员信息输入
                [3] 经理信息输入
                [4] 销售经理信息输入
                [5] 显示所有人工资信息
                [0] 退出
                ------------------------ 
            """)
            choice = int(input("请输入你的选择："))
            if choice == 1:
                self.inpworkers()
            elif choice == 2:
                self.inpsales()
            elif choice == 3:
                self.inpmanager()
            elif choice == 4:
                self.inpsalesmanager()
            elif choice == 5:
                self.allperson()
            elif choice == 0:
                print("谢谢使用!!")
                break
    def inpworkers(self):
        print("请输入工人信息（按工号，姓名，工作小时数，时薪输入）：")
        info = self.__get_data()
        workers = Workers(*info)
        self.workerslist.append(workers)

    def inpsales(self):
        print("请输入销售员信息（按工号，姓名，销售额，提成比例）：")
        info = self.__get_data()
        sales = Sales(*info)
        self.workerslist.append(sales)

    def inpmanager(self):
        print("请输入工人信息（按工号，姓名，固定月薪）：")
        info = self.__get_data()
        manager = Manager(*info)
        self.workerslist.append(manager)

    def inpsalesmanager(self):
        print("请输入工人信息（按工号，姓名，工作小时数，时薪输入）：")
        info = self.__get_data()
        salesmanager = SalesManager(*info)
        self.workerslist.append(salesmanager)

    def allperson(self):
        for i in self.workerslist:
            print(i)

    def __get_data(self):
        info = input()
        info = [x for x in info.split(" ") if len(x) > 0]
        return info

# if __name__ == '__main__':
ms = ManageSystem()
ms.choice()

# 10001 工人1号 8 20

