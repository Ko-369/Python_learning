# 定义集合
from polars import element

my_set = {"hello","world","hello world","hello","world","hello world","hello","world","hello world"}
my_set_empty = set()     # 定义空集合
print(f"my_set的内容是{my_set},类型是{type(my_set)}")
print(f"my_set的内容是{my_set_empty},类型是{type(my_set_empty)}")

# 添加新元素
my_set.add("python")
print(f"my_set添加元素后结果是：{my_set}")

# 移除元素
my_set.remove("python")
print(f"my_set移除python元素后结果是：{my_set}")

# 随机取出一个元素
element = my_set.pop()
print(f"my_set被随机取出的元素是{element},取出元素后：{my_set}")

# 清空集合
my_set.clear()
print(f"my_set清空后结果是：{my_set}")

# 取2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是：{set3}")
print(f"取出差集后原有set1的内容{set1}，原有set2的内容{set2}")

# 消除2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference_update(set2)   # 消除集合1内和集合2相同的元素
# 结果：集合1被修改，集合2不变
print(set1)
print(set2)


# 2个集合合并为1个
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(set3)

# 统计集合元素数量
set1 = {1,2,3,4,5}
num = len(set1)
print(f"集合set1中的元素数量是：{num}")

# 集合的遍历
# 集合是无序的，去重的，不能用while循环去遍历，但可以用for循环
set1 = {1,2,3,4,5}
for element in set1:
    print(f"set1中的元素有{element}")

