# 在控制台连续输出五行 * ✳️ ，每一行星号的数量依次递增
"""
*
**
***
****
*****
"""
row = 1
while row <= 9:
    # 增加一个小的循环，专门负责当前行中，每一"列"的星星显示
    # 1.定义一个列计数器变量
    col = 1
    while col <= row:
        # print('%d' % col)
        print('*', end='')
        col += 1

    # print('第 %d 行' % row)
    print('')

    row += 1
