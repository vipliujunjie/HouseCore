# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("\n\n\n" + "*" * 50)
    print("欢迎使用【名片管理系统】V1.0\n")
    # print("请直接输入菜单前面的【数字】选择要使用的功能\n")
    print("1.新增名片📇")
    print("2.显示全部🧵")
    print("3.搜索名片🔍")
    print("")
    print("0.退出系统")
    print("*" * 50 + "\n")


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成功
    print("%s的名片添加成功！" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")

        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果 return 后面没有任何的内容，表示会返回到调用函数的位置
        # 并且不会返回任何的结果
        return
    # 打印表头

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")

    print("")
    print("=" * 50)

    # 打印分割线
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card_dict["name"],
                                                    card_dict["phone"],
                                                    card_dict["qq"],
                                                    card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("🔍请输入需要搜索的姓名:")

    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:

        if card_dict["name"] == find_name:
            print("找到啦")
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            #  针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到 %s" % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """
    print(find_dict)
    action_str = input("请选择要执行的操作 "
                       "[1] 修改  [2] 删除  [0] 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "手机号：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("删除名片成功")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则返回原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户的的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回字典中 "原有的值"
    else:
        return dict_value

    # pass
