# 打开文件，不存在的文件
f = open("D:/test1.txt","a",encoding="UTF-8")

# write 写入
f.write("程序员小白")

# flush 刷新
f.flush()

# close 关闭
f.close()


# 打开一个存在的文件
f = open("D:/test1.txt","a",encoding="UTF-8")
# write 写入 ， flush 刷新
f.write("\nHello Python!!!")

# close 关闭
f.close()

