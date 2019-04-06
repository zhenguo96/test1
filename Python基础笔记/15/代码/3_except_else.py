try:
    print(5/0)
except ZeroDivisionError as e:
    print(e)
except ArithmeticError as e:
    print(e)
else:
    print("如果没有异常，则走else")
print("--"*30)











