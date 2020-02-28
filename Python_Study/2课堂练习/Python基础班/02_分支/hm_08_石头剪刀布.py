# 导入随机工具包
import random

# 从控制台输入要出的拳  —— 石头（1）  剪刀（2）   布（3）
player = int(input('\n\n请输入你要出的拳 - 石头（1）  剪刀（2）   布（3）：'))

# 电脑  随机 出拳 - 先假定电脑只会出石头，完整体代码功能
computer = random.randint(1, 3)
play = ''
if player == 1:
    play = '石头'
elif player == 2:
    play = '剪刀'
elif player == 3:
    play = '布'

comp = ''
if computer == 1:
    comp = '石头'
elif computer == 2:
    comp = '剪刀'
elif computer == 3:
    comp = '布'


# 比较胜负
if (    (player == 1 and computer == 2) or
        (player == 2 and computer == 3) or
        (player == 3 and computer == 1)):
    print('\n电脑弱爆了！\n')

elif (player == computer):
    print('\n平局！\n')

else:
    print('\n人类弱爆了！\n')

# 结果
print('\n\033[5;30;41m\t你出的拳头是 %s    \033[0m VS \033[0;30;44m\t  电脑出的拳是 %s   \033[0m' % (play, comp))