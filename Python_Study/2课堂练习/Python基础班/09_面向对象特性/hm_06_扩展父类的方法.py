class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def brak(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")

    def brak(self):
        # 1、针对子类特有需求编写代码
        print("叫的跟神一样...")

        # 2、使用super(). 调用原本在父类中封装的方法
        super().brak()

        # 父类名.方法(self)
        Dog.brak(self)

        # 注意：如果使用子类调用方法，会出现递归调用 -死循环
        # XiaoTianQuan.brak(self)

        # 3、增加其他子类代码
        print("@#$%##$#**")


xtq = XiaoTianQuan()

# 如果在子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xtq.brak()
