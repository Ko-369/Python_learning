# 字典中的元素是一个一个的键值对
# 语法： {key:vlaue, key:value ,…… ,key:value}
my_dict1 = {"张三":99,"李四":88,"李明":77}
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是{my_dict1},类型：{type(my_dict1)}")
print(f"字典1的内容是{my_dict2},类型：{type(my_dict2)}")
print(f"字典1的内容是{my_dict3},类型：{type(my_dict3)}")

# 字典不允许重复值出现，如果一个key对应了两个value，后面的会覆盖前面的
# 字典无法使用下标索引取值，只能通过key值取对应的value
my_dict1 = {"张三":99,"李四":88,"李明":77}
score = my_dict1["张三"]
print(f"张三的考试成绩是{score}")
score = my_dict1["李四"]
print(f"李四的考试成绩是{score}")
score = my_dict1["李明"]
print(f"李明的考试成绩是{score}")

# 字典的嵌套
# 字典的 key 可以是除字典外的其他任意数据类型， value 可以是任意数据类型（包括字典）
score_dict = {"张三":{"语文":77,
                  "数学":66,
                  "英语":33},
          "李四":{"语文":88,
                  "数学":86,
                  "英语":55},
          "李明":{"语文":99,
                  "数学":96,
                  "英语":66}
          }
print(f"学生的考试成绩是{score_dict}")

# 从嵌套字典获取数据

score = score_dict["张三"]["数学"]
print(f"张三的数学成绩是：{score}")
