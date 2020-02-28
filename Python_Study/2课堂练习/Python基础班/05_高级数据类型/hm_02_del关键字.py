name_list = ["张三", "李四", "王五"]

# del 关键字的用法（delete）删除列表元素
del name_list[0]

# del 关键字本质上是用来将 一个变量从内存中删除的
name = "小明"

del name
# 注意：如果使用del 关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了

print(name)     # 错误在这

print(name_list)
