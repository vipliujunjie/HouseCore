import time

def task_1():
    while True:
        print("---1---")
        time.sleep(0.1)
        yield

def task_2():
    while True:
        print("---2---")
        time.sleep(0.1)
        yield

def main():
    t1 = task_1()
    t2 = task_2()

    # 先让 t1 运行一会，当 t1 中遇到 yield 的时候，再返回到24行，
    # 然后执行 t2 ,当它遇到 yield 的时候，再次切换到 t1中
    # 这样 t1 t2 / t1 t2 的交替运行，最终实现了多任务....协程

    while True:
        next(t1)
        next(t2)

if __name__ == '__main__':
    main()

