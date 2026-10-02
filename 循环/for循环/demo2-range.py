# range语法1 range(num)
for x in range(10):
    print(x)

# range语法2 range(num1,num2)
# 从num1开始，到num2结束，但不会包括num2
for x in range(5,10):
    print(x)

# range 语法3 range(num1,num2,step)
# 从num1开始，到num2结束，但不会包括num2
# 数字之间的间隔是step
for x in range(5,10,2):
    print(x)

num = 100
count = 0
for x in range(1,100):
    if x % 2 == 0:
        count += 1

print(count)