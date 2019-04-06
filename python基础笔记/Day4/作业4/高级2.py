'''
2. 写一个程序模拟反复抛硬币，直到连续出现三次正面或反面为止，此时你的程序应该显示抛硬币的总次数。
    国徽向上！
国徽向上！
国徽向下！
国徽向上！
国徽向上！
国徽向下！
国徽向下！
国徽向上！
国徽向上！
国徽向上！
===================================================
总共抛了 10 次！
'''
import random
list = []
while True:
    jieguo = random.randint(0,1)
    list.append(jieguo)
    if jieguo == 1:
        print("国徽向上")
    elif jieguo == 0:
        print("国徽向下")
    if len(list) >= 3:
        for i in range(len(list)-2):
            if list[i] == list[i + 1] == list[i + 2]:
                print("总共抛了%d次" % len(list))
                quit()








