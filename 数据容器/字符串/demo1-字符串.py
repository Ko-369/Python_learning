# 通过下标索引取值
my_str = "hello world"
print(my_str[3],my_str[-5])

# index 方法
print(my_str.index("l"))

# replace 方法： 将字符串中的 全部 字符串1，替换为 字符串2
# 注意：replace 方法不是修改字符串本身，而是得到一个新的字符串
new_my_str = my_str.replace("l","k")
print(new_my_str)

# split 方法：  按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 注意： 字符串本身不变，而是得到了一个列表对象
my_str = "hello world i am a new friend to leran python"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行切分后得到：{my_str_list}，类型是{type(my_str_list)}")

# strip 方法： 字符串的规整操作 去除首尾指定字符串
my_str = "    Hello World    "
new_my_str = my_str.strip()
print(f"字符串{my_str}被strip后，结果是：{new_my_str}")
my_str = "12Hello World21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后，结果是：{new_my_str}")

# count 方法： 统计字符串中某字符串的出现次数
my_str = "hello world hello world hello world"
print("he出现的次数是：",my_str.count("he"))

# 统计字符串的长度，len()
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")