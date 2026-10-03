# 元组一经定义，不可修改
# 定义元组
t1 = (1,"hrllo",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}，内容是：{t1}")
print(f"t2的类型是：{type(t2)}，内容是：{t2}")
print(f"t3的类型是：{type(t3)}，内容是：{t3}")

# 定义单个元素的元组  一定要在元素后面写一个 逗号
t4 = ("Hello",)

# 元组嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是{t5}")
print(t5[1][2])

# 元组的操作： index 查找方法
t6 = ("hello","world","Hello World")
print(t6.index("world"))

# 元组的操作： count 统计方法
t7 = ("hello","world","Hello World","hello","world","Hello World")
print(t7.count("world"))

# 元组的操作： len 函数统计元组元素数量
t8 = ("hello","world","Hello World","hello","world","Hello World")
print(len(t8))

# 元组的遍历： while
index = 0
while index < len(t8):
    print(t8[index])
    index += 1

# 元组的遍历： for
for i in range(len(t8)):
    print(t8[i])

# 注意：如果在元组种嵌套了列表，列表中的内容可以修改
t9 = (1,2,["hello","world","Hello World"])
print(f"t9的内容是{t9}")
t9[2][2] = "你好，世界。"
print(f"t9的内容是{t9}")


