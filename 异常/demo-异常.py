# # 异常的基本捕获语法
# try :
#     f = open("D:/abc.txt","r",encoding = "UTF-8")
# except:
#     print("出现异常了，因为文件不存在，我将open的模式改为w模式去打开")
#     f = open("D:/abc.txt","w",encoding = "UTF-8")
#
# # 捕获指定的异常
# try:
#     print(name)
#     # 1 / 0
# except NameError as e:
#     print("出现了变量未定义的异常。")
#     print(e)
#
# # 捕获多个异常
# try:
#     print(name)
#     # 1 / 0
# except (NameError,ZeroDivisionError) as e:
#     print("出现了变量未定义 或者 除以0的异常错误。")
#     print(e)

# 捕获所有异常
# try:
#     f = open("D:/abc.txt","r",encoding = "UTF-8")
# except Exception as e:
#     print("出现异常了")
# else:
#     print("没有异常，好开心。")
# finally:
#     print("我是finally，有没有异常我都会执行")
#     f.close()

# 异常具有传递性
def func1():
    print("func1开始执行")
    num = 1 / 0         # 除以0的异常
    print("func1结束执行")

# 定义一个无异常的方法，调用上面的方法
def func2():
    print("func1开始执行")
    func1()
    print("func1结束执行")

# 定义一个方法，调用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常的信息是：{e}")


main()

