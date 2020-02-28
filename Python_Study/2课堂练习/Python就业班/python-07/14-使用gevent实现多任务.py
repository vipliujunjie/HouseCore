import gevent
import time

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep()

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep()

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep()


print("---1---")
g1 = gevent.spawn(f, 5)
print("---2---")
g2 = gevent.spawn(f, 5)
print("---3---")
g3 = gevent.spawn(f, 5)
print("---4---")

g1.join()
g2.join()
g3.join()

