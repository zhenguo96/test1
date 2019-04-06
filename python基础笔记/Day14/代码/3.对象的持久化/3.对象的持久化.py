# pickle
import pickle

# pickle持久化必须是二进制文件
# 写文件
# with open("list1.txt","wb") as fp:
#     pickle.dump([1,2,3],fp)

# 读文件
# with open("list1.txt","rb") as fp:
#     list1 = pickle.load(fp)
#     print(list1)

import dbm
#写文件
# with dbm.open("db1","c") as db:
#     # 键必须是字符串，值必须是字节字符串
#     db['name'] = b'tom'
#     db['age'] = str(19).encode('utf-8')

# with dbm.open('db1') as db:
#     for key in db:
#         print(db[key].decode('utf-8'))


import shelve
# 写文件
# with shelve.open('s1','c') as sh:
#     sh['grade'] = (90,98,97)
#     sh['name'] = "黑马"
#     sh['age'] = 20

# 读文件
# with shelve.open('s1') as sh:
#     for key in sh:
#         print(sh[key])

# 更新
# writeback 置为True
with shelve.open('s1',writeback=True) as sh:
    for key in sh:
        sh['age'] = 18
        print(sh[key])




