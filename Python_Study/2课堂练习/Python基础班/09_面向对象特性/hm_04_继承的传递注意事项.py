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

class Cta(Animal):
    def catch(self):
        print("抓老鼠")


# 创建一个对象，啸天犬
xtq = XiaoTianQuan()

mao = Cta()

xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()
xtq.brak()
xtq.fly()

mao.catch()
