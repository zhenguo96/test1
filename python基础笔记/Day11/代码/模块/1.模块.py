# 搜索路径

# 导入同一个包中的模块
# from 包名1.包名2...模块1 import 标识符（变量名、函数名）
# 一行引入多个标识符
# 导入模块中所有的标识符
# from A1.mk1 import *    # 不建议

# 给指定标识符起别名
from A1.mk1 import a as a1
from A1.mk1 import say as hello

print(a)
print(a1)
hello()




