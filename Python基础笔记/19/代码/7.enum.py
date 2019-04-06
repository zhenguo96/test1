from enum import Enum,IntEnum,unique
# 自定义枚举常量
@unique     # 唯一，不允许成员有重复值
class Color(Enum):
    RED = 0
    BLUE = 1

# 不能修改
# Color.RED = 10
print(Color.RED.name)




















