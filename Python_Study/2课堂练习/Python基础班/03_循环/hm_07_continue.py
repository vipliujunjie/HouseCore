# 循环 跳出 循环 continue
i = 0

while i <= 10:
    # if i % 2 != 0: continue取余
    if i == 3:
        # 注意：在循环中，如果使用continue 这个 关键字
        # 在使用关键字之前，需要确认循环的计数是否修改，
        # 否则可能会导致死循环
        i += 1
        continue

    print(i)
    i += 1
print('over')
