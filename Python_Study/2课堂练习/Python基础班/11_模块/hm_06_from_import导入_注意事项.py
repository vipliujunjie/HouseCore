# 导入同名模块 -如果有两个模块名相同，后导入的会覆盖先导入的
# from hm_01_测试模块1 import say_hello

from hm_01_测试模块1 import say_hello as module1_say_hello
from hm_02_测试模块2 import say_hello

module1_say_hello()
say_hello()
