# 打开文件，不存在的文件
import time

# f = open("D:/test.txt","w",encoding="UTF-8")    # 如果打开的问价不存在，会自动创建一个新文件
# # write 写入
# f.write("Hello World!!!")      # 内容写入到内存中
#
# # flush 刷新
# f.flush()
#
# # close 关闭
# f.close()   # close 内置flush功能，如果不调用flush，但调用close，内容同样能被写入文件

# 打开一个存在的文件
f = open("D:/test.txt","w",encoding="UTF-8")

# write 写入，flush 刷新
f.write("程序员小白")  # 如果文件已经存在，再用w去写，会把原有内容清空，把新的内容写进去

# close 关闭
f.close()