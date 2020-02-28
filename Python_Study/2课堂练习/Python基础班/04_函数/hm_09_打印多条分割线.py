def print_line(char, times):
    """分割线"""

    print(char * times)


def print_lines(char, times):
    """多行分割线
    :param char: 字符
    :param times: 字数
    """
    row = 0

    while row < 5:
        print_line(char, times)
        row += 1


print_lines("-", 50)


'''我的自定义输入'''

# def print_line(char, times):
#     # 分割线
#
#     print(char * times)
#
#
# def print_lines(char, times, height):
#     row = 0
#
#     while row < height:
#         print_line(char, times)
#         row += 1
#
#
# print_lines(input("字符："), int(input("字数："), int(input("行数："))))
