def list_while_func():
    """
    使用while循环便利列表的演示函数
    :return: None
    """
    my_list = ["hello","world","python"]
    # 循环控制变量童年过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量
    index = 0
    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1

list_while_func()


def list_for_func():
    mylist = [1,2,3,4,5,6]
    for i in range(len(mylist)):
        element = mylist[i]
        print(f"列表的元素：{element}")

list_for_func()

def func():
    _list = [1,2,3,4,5,6,7,8,9,10]
    list1 = []
    for i in range(len(_list)):
        if _list[i] % 2 == 0:
            list1.append(_list[i])

    print(list1)


func()