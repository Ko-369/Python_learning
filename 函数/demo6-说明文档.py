def add(x,y):
    """
    add 函数可以接收2个参数，进行2数相加的功能
    :param x: 形参 x 表示相加的其中一个数字
    :param y: 形参 y 表示相加的另一个数字
    :return: 返回值是两数相加的结果
    """
    result = x + y
    print(f"两数相加的结果是：{result}")
    return  result

add(5,6)