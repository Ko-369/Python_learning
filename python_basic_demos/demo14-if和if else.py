from encodings.punycode import adapt

print("欢迎来到儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元。")

print("祝您游玩愉快")

print("欢迎来到儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已成年，游玩需要补票10元。")
else:
    print("您尚未成年，可以免费游玩。")

print("祝您游玩愉快")

print("欢迎来到动物园。")
height = int(input("请输入您的身高（cm）："))
if height >= 120:
    print("您的身高超出120cm，游玩需要补票10元。")
else:
    print("您的身高尚未超出120cm，可以免费游玩。")

print("祝您游玩愉快")



