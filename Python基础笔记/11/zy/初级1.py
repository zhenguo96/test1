# 用列表生成式完成，l1 = ['Java' , 'C' , 'Swift' , 'Python' , True,12.4],请将l1中字符串全部转换为小写，其他项不动
l1 = ['Java' , 'C' , 'Swift' , 'Python' , True,12.4]
l2 = [i.lower() if type(i) == str else i for i in l1 ]
print(l2)








