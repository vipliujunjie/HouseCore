class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    # 对象销毁前执行的方法
    def __del__(self):

        print("%s 去了" %  self.name)

# Tom 是一个全局变量
tom = Cat("tom")
print(tom.name)

# del tom

print("-" * 50)
