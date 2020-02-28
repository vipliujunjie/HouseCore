hello_str = "Hello Hello"

# 1.统计字符串长度
print("长度:%s" % (len(hello_str)))

# 2.统计某一个小字符串出现的次数
print("出现'llo'的次数:%s" % (hello_str.count("llo")))
print("出现'abc'的次数:%s" % (hello_str.count("abc")))

# 3.某一个子字符串出现的位置
print("出现'e'的位置:%s" % (hello_str.index("e")))

# 注意：如果使用index方法传递的子字符串不存在，程序会报错
print("出现'e'的位置:%s" % (hello_str.index("q")))
