# 定义好函数后，只表示这个函数封装了一段代码而已
# 如果不主动调用函数，函数 是不会主动执行的


name = "小明"
def say_hello():
    """打招呼"""

    print("Hello Python 1")
    print("Hello Python 2")
    print("Hello Python 3")

print(name)

say_hello()

print(name)
