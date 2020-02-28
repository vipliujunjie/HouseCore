hello_str = "hello world"

# 1.判断是否以指定字符串开始
print(hello_str.startswith("h"))

# 2.判断是否以指定字符串结束
print(hello_str.endswith("d"))

# 3.查找指定字符串
print(hello_str.find("o"))
# index ->如果指定的字符串不存在，会报错
# find  ->如果指定的字符串不存在，会返回 -1
print(hello_str.find("abc"))

# 4.替换字符串             旧的       新的
# replace方法会返回一个新的字符串
# 不会修改原有字符串的内容
print(hello_str.replace("world", "Python"))

print(hello_str)
