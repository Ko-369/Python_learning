# 打开文件
import time

f = open("D:\人生难只如初见 - 副本.txt","r",encoding="UTF-8")
print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果：{f.read()}")


# 读取文件 - readLines()
# lines = f.readlines()
# print(f"lines对象的类型是：{type(lines)}")
# print(f"lines对象的内容是：{lines}")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是{line1}")
# print(f"第二行数据是{line2}")
# print(f"第三行数据是{line3}")


# for 循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")


# 文件的关闭

f.close()     # 关闭文件，接解除文件的占用


# with open 语法操作文件   with open 在使用完文件后会自动关闭
with open("D:\人生难只如初见 - 副本.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

