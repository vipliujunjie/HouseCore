xiaoming_dict = {"name": " 小明"  ,
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量 K 是每一次循环中，获取到的键值对的Key
for k in xiaoming_dict:
    print("%06s 对应 %s" % (k, xiaoming_dict[k]))
