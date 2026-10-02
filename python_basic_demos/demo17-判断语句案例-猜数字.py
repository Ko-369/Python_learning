"""
猜数字
"""

# 1.构建一个随机的数字变量

import random

random_num = random.randint(1, 10)

guess_num = int(input("请输入你要猜测的数字（1到10）：\n"))

# 2.通过if判断语句尽心那个数字的猜测

if guess_num == random_num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > random_num:
        print("你猜测的数字大了。")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("请输入第二次你要猜测的数字（1到10）：\n"))

    if guess_num == random_num:
        print("恭喜，第二次就猜中了")
    else:
        if guess_num > random_num:
            print("你猜测的数字大了。")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("请输入第三次你要猜测的数字（1到10）：\n"))

        if guess_num == random_num:
            print("恭喜，第三次猜中了")
        else:
            print("三次机会用完了，没有猜中。")
