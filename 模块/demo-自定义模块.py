# 导入自定义模块使用
# import my_moduel1
# my_moduel1.test(3,6)

# 导入不同模块的同名模块    后面的会直接覆盖前面的，前面的不被使用
# from my_moduel1 import test
# from my_moduel2 import test
#
# test(3,6)
# test(3,6)

from my_moduel1 import *
test_a(1,2)

