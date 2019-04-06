class Students():
    def __init__(self,name,stuid,age,gender):
        self.name = name
        self.stuid = stuid
        self.age = age
        self.gender = gender
    def learn(self,subjects):
        print("{}学习的内容为：{}".format(self.name,subjects))
class Pupil(Students):
    def fight(self):
        print("打架中。。。")
class Middle(Students):
    def love(self):
        print("恋爱中。。。")
class College(Students):
    def play(self):
        print("逃课中。。。")
pupil = Pupil("小学生1号",10001,9,"女")
pupil.learn("语文 数学 英语")
middle = Middle("中学生1号",20001,15,"男")
middle.learn("语数外 生物化 史地政")
college = College("大学生1号",30001,19,"女")
college.play()

