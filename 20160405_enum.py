#使用枚举

from enum import Enum, unique

# 定义一个枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'))

# 遍历枚举
for name, month in Month.__members__.items():
	print(name, '->', month, '->', month.value)


jan = Month.Jan
print(jan.value)

print(jan == Month.Jan)

# 定义一个枚举

# 定义枚举的时候不允许key与value出现重复，否则在定义时就会报错
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

# 根据枚举的成员名称来取值
print(Weekday.Sat.value)

# 根据value来获取枚举常亮
print(Weekday(6))

# 获取枚举中不存在的值直接报错
print(Weekday.Jan)
print(Weekday(7))