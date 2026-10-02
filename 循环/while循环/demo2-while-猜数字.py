# import random
# num = random.randint(1,100)
# guess_num = int(input("请输入你猜测的数字（1-100）：\n"))
#
# count = 1
#
# while guess_num != num:
#     if guess_num > num:
#         guess_num = int(input("太大了，再猜一次吧！"))
#     else:
#         guess_num = int(input("太小了，再猜一次吧！"))
#     count += 1
#
# print(f"恭喜你猜中了！你一共猜了{count}次。")



import random
num = random.randint(1,100)
count = 0
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字：\n"))
    count += 1
    if guess_num == num:
        print("猜中了！")
        # 设置False为终止循环的条件
        flag = False
    else:
        if guess_num > num:
            print("太大了")
        else:
            print("太小了")

print(f"你总共猜了{count}次")