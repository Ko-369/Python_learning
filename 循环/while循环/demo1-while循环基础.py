# 循环一定要设置终止条件，不然会无限循环
i = 0
while i < 100:
    print(f"{i}小美，我喜欢你！")
    i += 1

num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
print(f"1-100累加的和是：{sum}")
