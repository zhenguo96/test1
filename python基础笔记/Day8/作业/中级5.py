# 5.每个学生都有如下信息：学号、姓名、年龄，班级。
# （1）	请设计一个函数完成输入一个班级的学生信息，参数为班级人数，返回值为包含学生信息的列表

# def grade(n):
#     students = dict(id=[],name=[],age=[],grade=[])
#     for i in range(n):
#         id = input("学号：")
#         name = input("姓名：")
#         age = input("年龄：")
#         grade = input("班级：")
#         students["id"].append(id)
#         students["name"].append(name)
#         students["age"].append(age)
#         students["grade"].append(grade)
#     for j in range(len(students["id"])):
#         a = []
#         a.append(students["id"][j])
#         a.append(students["name"][j])
#         a.append(students["age"][j])
#         a.append(students["grade"][j])
#         print(a)
# res = grade(3)

# （2）	请设计一个函数完成按学号查询学生信息，参数是学号，返回值为学生信息
# def chaxun(id1):
#     students = {"id":['10001','10002','10003'],
#                 "name":['lilei','hanmeimei','tom'],
#                 "age":['21','22','23'],
#                 "grade":['1902','1901','1902']
#                 }
#     name = students["name"][students["id"].index(id1)]
#     age = students["age"][students["id"].index(id1)]
#     grade = students["grade"][students["id"].index(id1)]
#     print("学号：%s，姓名：%s，年龄：%s，班级：%s" % (id1,name,age,grade))
# res = chaxun('10001')

# （3）	请设计一个函数，对学生信息按年龄排序，无参无返回值
students = {"id":['10001','10002','10003'],
            "name":['lilei','hanmeimei','tom'],
            "age":['21','22','23'],
            "grade":['1902','1901','1902']
            }





