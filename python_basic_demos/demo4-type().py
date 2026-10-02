# 使用 print 直接输出数据类型信息
print(type("Hello World!"))
print(type(666))
print(type(13.14))

# 使用变量存储 type() 语句的结果
string_type = type("Hello World!")
int_type = type(666)
float_type = type(13.14)

print(string_type)
print(int_type)
print(float_type)


# 使用 type() 语句，查看变量中存储的数据类型信息

name = "name"
name_type = type(name)

print(name_type)