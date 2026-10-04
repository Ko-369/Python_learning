my_dict = {"张三": 99, "李四": 88, "李明": 77}
# 字典新增元素
my_dict["小亮"] = 66
print(f"字典经过新增元素后，结果：{my_dict}")

# 更新元素
my_dict["张三"] = 33
print(f"字典经过更新后，结果：{my_dict}")

# 删除元素
score = my_dict.pop("张三")
print(f"字典中被移除了一个元素，结果：{my_dict},张三的考试分数是：{score}")

# 清空元素
my_dict.clear()
print(f"字典清空后的结果：{my_dict}")

# 获取全部key
my_dict = {"张三": 99, "李四": 88, "李明": 77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")

# 遍历字典
# 方式1
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 方式2
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{my_dict[key]}")

# 统计字典元素数量，len()函数
num = len(my_dict)
print(f"字典中的元素数量有：{num}个")

