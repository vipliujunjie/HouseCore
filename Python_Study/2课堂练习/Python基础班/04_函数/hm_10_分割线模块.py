def print_line(char, times):
    """分割线

    :param char: 字
    :param times: 数
    """
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


name = "黑马程序员"
