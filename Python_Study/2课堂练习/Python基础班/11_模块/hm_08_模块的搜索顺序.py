# ⚠️注意️：在开发时，给文件起名不要和 系统的模块文件重名

import random

# __file__ 可以 查看 当前 导入模块 对应的 完整路径
print(random.__file__)

rand = random.randint(0, 10)

print(rand)
