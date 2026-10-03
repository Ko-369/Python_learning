def say_hi():
    print("你好呀！")

result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

def say_hi2():
    print("你好呀！")
    return None

result2 = say_hi2()
print(f"无返回值函数，返回的内容是：{result2}")
print(f"无返回值函数，返回的内容类型是：{type(result2)}")
