class Cat:

    def __init__(self, new_name):   # 初始化__init__

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):              # 对象销毁前执行的方法

        print("%s 去了" % self.name)

    def __str__(self):              # 这是一个对象字符串方法

        # 必须返回一个字符串
        return "我是小猫【%s】" % self.name

# Tom 是一个全局变量
tom = Cat("Tom")

print(tom)
