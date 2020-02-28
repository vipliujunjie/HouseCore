# 导入随机工具包
import random
player_f = 0
computer_f = 0

# 从控制台输入要出的拳  —— 石头（1）  剪刀（2）   布（3）
button = 'on'
while button == 'on':
    player = input('\n\n\n\n\n\n请输入你要出的拳 - 石头（1）  剪刀（2）   布（3）：')
    if player == 'off':
        button = 'off'
        break
    elif player == "1" or "2" or "3":
        pk()
    else:
        print('\n指令错误，输入 off 关闭，其他无效')
        button = 'on'
        continue
    def pk():
        # 电脑  随机 出拳 - 先假定电脑只会出石头，完整体代码功能
        computer = random.randint(1, 3)
        play = ''
        if player == '1':
            play = '石头'
        elif player == '2':
            play = '剪刀'
        elif player == '3':
            play = '布'

        comp = ''
        if computer == 1:
            comp = '石头'
        elif computer == 2:
            comp = '剪刀'
        elif computer == 3:
            comp = '布'


        # 比较胜负
        if (    (int(player) == 1 and computer == 2) or
                (int(player) == 2 and computer == 3) or
                (int(player) == 3 and computer == 1)):
            player_f += 1
            computer_f -= 1
            print('\n\n\n电脑弱爆了！')
            print('\n\033[0;37;41m\t你出的拳头是 %s    \033[0m VS \033[5;37;44m\t  电脑出的拳是 %s   \033[0m' % (play, comp))
            print("\n\033[0;37;44m\t电脑分数 -1 \033[0m")
            print("玩家当前分数 %d ，电脑当前分数 %d " % (player_f, computer_f))

        elif (int(player) == computer):

            print('\n\n\n平局！\n')
            print('\n\033[0;37;41m\t你出的拳头是 %s    \033[0m VS \033[0;37;44m\t  电脑出的拳是 %s   \033[0m' % (play, comp))
            print("\n玩家当前分数 %d ，电脑当前分数 %d " % (player_f, computer_f))

        else:
            player_f -= 1
            computer_f += 1
            print('\n\n\n玩家弱爆了！')
            print('\n\033[5;37;41m\t你出的拳头是 %s    \033[0m VS \033[0;37;44m\t  电脑出的拳是 %s   \033[0m' % (play, comp))
            print("\n\033[0;37;41m\t玩家分数 -1 \033[0m")
            print("玩家当前分数 %d ，电脑当前分数 %d " % (player_f, computer_f))
        # 结果
        #print('\n\033[0;37;41m\t你出的拳头是 %s    \033[0m VS \033[0;37;44m\t  电脑出的拳是 %s   \033[0m' % (play, comp))
