def measure():
    """测量温度和湿度"""

    print("测量开始。。。")
    temp = 30
    wetness = 50
    print("测量结束。。。")

    # 元组可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如函数返回的类型是元组，小括号可以省略
    # return (temp, wetness)
    return temp, wetness


# 元组
result = measure()
print(result)

# 需要单独的处理温度或湿度 - 不方便
print(result[0])
print(result[1])
print("温度是：%s，湿度是：%s" % (result[0], result[1]))

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回结果
# 注意：使用多个变量接收结果时，变量的个数，应该和元组中元素的个数，保持一致
gl_temp, wetness = measure()

print(gl_temp, wetness)
