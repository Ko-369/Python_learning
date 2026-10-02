print("欢迎来到动物园")

if int(input("请输入你的身高（cm）：")) > 120 :
    print("你的身高大于120cm，不可以免费")
    print("但如果你的vip等级高于3，可以免费游玩")
    if int(input("请输入你的vip等级:")) > 3 :
        print("恭喜你，你的vip等级高于3，可以免费游玩")
    else:
        print("Sorry,你需要补票10元。")
else:
    print("你是小朋友，可以免费游玩")





age = int(input(("请输入你的年龄")))
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if int (input("请输入你的入职时间：")) > 2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物。")
        elif int (input("请输入你的级别：")) > 2:
            print("恭喜你，年龄和级别都达标，可以领取礼物。")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标")
    else:
        print("不好意思，年龄太大了。")

else:
    print("不好意思，小朋友不可以领取。")



age = int(input("请输入你的年龄："))
if  age>= 18 & age < 30:
    if int(input("请输入你的入职年份：")) > 2:
        print("欢迎您领取奖励！")
    elif int(input("请输入您的等级：")) > 3:
        print("欢迎您领取奖励！")

else:
    print("Sorry，您不能领取奖励。")

age = int(input("请输入你的年龄："))
if (age >= 18 and age < 30) & (int(input("请输入你的入职年份：")) > 2 or int(input("请输入您的等级：")) > 3):

    print("欢迎您领取奖励！")

else:
    print("Sorry，您不能领取奖励。")

"""
&(按位与运算符)不能用于逻辑运算，它的逻辑是直接将其两边的值先转换成二进制，然后进行按位与操作，
一些代码用这个符号进行逻辑运算能跑出来，并且结果也对，是因为巧合，
在语法上合规不会报错，但在逻辑上是错的，
进行逻辑运算要用and
"""
a = 2
b = 4
if a >1 & b >3:
    print("满足条件")
else:
    print("不满足条件")
