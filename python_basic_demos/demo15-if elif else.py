print("欢迎来到动物园。")
height = int(input("请输入你的身高（cm）"))
vip_level = int(input("请输入你的vip级别（1~5）"))
day = int(input("请告诉我今天是几号："))
if height < 120:
    print("您的身高小于120cm，可以免费游玩。")
elif vip_level > 3:
    print("您的vip级别大于3，可以免费游玩。")
elif day == 1:
    print("今天是1好免费日，可以免费。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")

print("祝您游玩愉快！")

if int(input("请输入你的身高（cm）")) < 120:
    print("您的身高小于120cm，可以免费游玩。")
elif int(input("请输入你的vip级别（1~5）")) > 3:
    print("您的vip级别大于3，可以免费游玩。")
elif int(input("请告诉我今天是几号：")) == 1:
    print("今天是1好免费日，可以免费。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")

print("祝您游玩愉快！")


num = 9
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你猜对了！")
elif int(input("没有猜对，再猜一次：")) == num:
    print("恭喜你猜对了！")
elif int(input("没有猜对，再猜一次：")) == num:
    print("恭喜你猜对了！")
else :
    print("Sorry，全部猜错了，我想的是：9")