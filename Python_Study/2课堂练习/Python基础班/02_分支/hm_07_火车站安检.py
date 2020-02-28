# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = int(input("\n检查车票："))

# 首先检查是否有车票，如果有，才允许进行 安检
if has_ticket == True:
    print('车票检查通过，请进入安检')

    # 定义整型变量 weixian 表示是否带危险物品
    weixian = int(input('是否带有危险物品：'))

    # 检查是否带有危险物品
    if weixian == True:

        # 定义整型变量 knife_length 表示刀的长度，单位：厘米
        knife_length = int(input('刀的长度：'))

        # 安检时，需要检查刀的长度，判断是否超过20厘米
        if knife_length > 20:
            # 如果超过20厘米，提示刀的长度，不允许上车
            print('\033[5;30;41m\t安检失败，你的刀长度为 %d 厘米，国家规定 20 厘米，超出规定 %d 厘米，不允许上车\033[0m' % (
            knife_length, knife_length - 20))
        # 如果不超过 20 厘米，安检通过
        elif weixian == True:
            print('\033[0;30;44m\t安检通过，你的刀长度为 %d 厘米，不超出国家规定的 20 厘米，余量 %d 厘米，请上车\033[0m' % (
            knife_length, 20 - knife_length))
    # 如果没有危险物品，请上车
    else:
        print('\033[0;30;44m\t没有携带危险物品，安检通过，请上车！\033[0m')

# 如果没有车票，不允许进门
else:
    print('没有检测到车票，请先买票！')
