
name_list = ["张三", "李四", "王五"]

# 1.取值和取索引
# IndexError: list index out of range -> 列表索引超出范围
print(name_list[2])

# 知道数据的内容，想确定数据在列表重的位置
# 使用index要注意，如果传递的数据不再列表中，程序会报错
print(name_list.index("王五"))

# 2.修改
name_list[1] = " 王麻子"

# IndexError: list assignment index out of range -> 列表指定的索引超出范围 ：索引错误
# name_list[3] = "李小二"

# 3.增加
# append 方法可以向列表的末尾增加数据
name_list.append("刘能")

# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(1, "傻逼")

# extend 方法可以把其他列表的内容追加到当前列表的末尾
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)

# 4.删除
# remove 方法可以从列表中删除指定的数据
name_list.remove("傻逼")

# pop 方法默认删除列表最后一个元素
name_list.pop()

# pop 方法可以索引删除指定元素
name_list.pop(0)

# clear 方法可以清空列表
name_list.clear()


print(name_list)
