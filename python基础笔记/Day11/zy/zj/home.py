from zy.zj.views import *
import time
while 1:
    print("******欢迎使用成绩管理系统********")
    print("[1] 学生信息输入")
    print("[2] 学生信息输出")
    print("[3] 查找学生信息")
    print("[4] 成绩排序")
    print("[0] 退出")
    print("------------------------")
    choice = int(input("请输入你的选择："))
    if choice == 1:
        shuru()
        print("操作成功！请稍后。。。")
    elif choice == 2:
        shuchu()
    elif choice == 3:
        chazhao()
    elif choice == 4:
        paixu()
    elif choice == 0:
        print("已退出！！")
        quit()
    else:
        print("选择有误！")
    time.sleep(2)
# dictstu = [['李四', '2009002', '86', '78','164','82'],['张三', '2009001', '85', '89','174','87']]
# students1 = "张三    2009001    85    89"
# students2 = "李四    2009002    86    78"









