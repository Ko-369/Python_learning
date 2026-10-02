"""Python 变量本质上是对象的引用绑定关系。
    变量名保存的是对象引用，
    而对象负责保存实际的数据和类型信息。
    变量不是存储数据的容器，而是指向对象的名字。
"""
from pymupdf import message

# 变量定义格式： 变量名 = 变量值

money = 50

print("余额还有：",money,"元。")

money -= 10
print(money)

money -= 10
print(money)

money -= 10
print(money)

message = "hello world"

print(message)

message = "你好 世界"

print(message)