from polars import element

my_list = ["hello","world","python"]
# 1.1 查找某元素在列表中的下标索引
index = my_list.index("python")
print(index)
# 1.2 如果被查找的元素不存在，会报错
# index = my_list.index("C++")
# print(index)

# 2 修改特定下标索引的值  语法：  列表[下标] = 值
my_list[2] = "C++"
print(my_list[2])

# 3 在指定下标位置插入新元素
my_list.insert(2,"python")
print(my_list[2])

# 4 在列表的尾部追加 单个 新元素
my_list.append("Java")
print(my_list)

# 5 在列表的尾部追加 一批 新元素
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(my_list)

# 6 删除指定下标索引的元素 （2种方式）
my_list = ["hello","world","python"]
# 6.1 方式1 ：     del 列表[下标]
del my_list[2]
print(my_list)

my_list = ["hello","world","python"]
# 6.2 方式2 ：     列表.pop[下标]
element = my_list.pop(2)
print(f"通过pop方法取出元素后列表内容：{my_list}，取出的元素是：{element}")

# 7 删除在列表中第一次出现的某元素
my_list = ['hello',2,'hello','hello','hello','hello', 'world', 'python', 'C++', 'Java', 1, 2, 3]
my_list.remove(2)
print(my_list)

# 8 清空列表
my_list.clear()
print(my_list)

# 9 统计列表内某元素的数量
my_list = ['hello',2,'hello','hello','hello','hello', 'world', 'python', 'C++', 'Java', 1, 2, 3]
count = my_list.count('hello')
print(f"count的数量是{count}")

# 10 统计列表中全部元素的数量
my_list = ['hello',2,'hello','hello','hello','hello', 'world', 'python', 'C++', 'Java', 1, 2, 3]
count = len(my_list)
print(f"列表的元素数量共有：{count}个")


_list = [21,25,21,23,22,20]
_list.append(31)
print(_list)
_list.extend([29,33,30])
print(_list)
print(_list[0])
print(_list[-1])
print(_list.index(31))
print(_list)


