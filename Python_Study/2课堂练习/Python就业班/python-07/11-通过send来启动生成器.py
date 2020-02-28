
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(">>>ret>>>>", ret)
        a, b = b, a + b
        current_num += 1

obj = create_num(10)

# obj.send(None)  # send一般不会放到第一次启动生成器，如果非要这样做 那么就传递None

ret = next(obj)
print(ret)

# send里面的数据会 传递给第五行，当作 yield a 的结果，然后 ret 保存这个结果...
# send的结果是下次调用 yield 时 yield后面的值
ret = obj.send("hahahahha")
print(ret)

