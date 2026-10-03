# 变量分为 ：局部变量 全局变量
# 局部变量 ：定义在函数体内部的变量，只能在函数体内部生效，临时保存数据，函数调用结束后被销毁
# 全局变量 ： 在函数体内、外都能生效的变量

# def demo_a():
#     num = 100
#     print(num)
#
# demo_a()

# print(num) 这个语句无法执行，会报错，原因是 num 是局部变量，该语句在函数之外，无法使用该变量

# 定义全局变量 num

# num1 = 200
# def demo_A():
#     num1 = 300
#     print(num1)
#
# demo_A()
# print(f"这是全局变量{num1}")

num = 200

def demo1():
    print(f"demo1:{num}")

def demo2():
    global num    # 设置内部定义的变量为全局变量
    num = 500
    print(num)

demo1()
demo2()
print(num)

