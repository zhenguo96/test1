class Student:
    def __init__(self,sname,sno,math,computer):
        self.sname = sname
        self.sno = sno
        self.math = math
        self.computer = computer
        self.total = self.math + self.computer
        self.avg = self.total / 2
    def __str__(self):
        return "{:6}\t{:12}\t{:4}\t{:4}\t{:4}\t{:4}".format(self.sno,self.sname,self.math,self.computer,self.total,self.avg)

if __name__ == "__main__":
    s1 = Student('李四','1001',89,98)
    print(s1)












