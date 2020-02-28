info_tuple = ("zhangsan", 18, 1.75, 18)

# 1.取值 和取索引
print("取值:%s" % info_tuple[0])

# 已经知道数据的内容，希望知道该数据 在元组中的索引
print("在元组中的索引:%s" % (info_tuple.index('zhangsan')))

# 2.统计计数
print("统计计数:%s" % (info_tuple.count(18)))

# 统计元组中包含元素的个数
print("元素的个数:%s" % (len(info_tuple)))
