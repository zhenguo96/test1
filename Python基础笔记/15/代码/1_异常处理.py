"""
try:
    print(5/0)
except errorType as e:
    todo
    
"""
try:
    print(5/0)
# 类型精确的except块放在前面
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
print("*"*50)















