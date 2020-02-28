xiaoming_dict = {"name": "小明"}

# 1.取值
print(xiaoming_dict["name"])
# 在 取值的时候，如果指定的 KEY 不存在，程序会报错！
# print(xiaoming_dict["name123"])


# 2.增加/修改  如果Key不存在就增加，如果Key存在就修改
xiaoming_dict["age"] = 18
# 修改
xiaoming_dict["name"] = "小小明"


# 3.删除
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错
# xiaoming_dict.pop("name123")

xiaoming_dict.pop("name")

print(xiaoming_dict)