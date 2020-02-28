# input_str = input("请输入：")

# print(eval(input_str))
# python -m pygame.examples.aliens
# conda info --envs
# source activate snakes

import pygame

# 使用pygame模块必须先调用pygame.init()来加载其他模块
pygame.init()

# 创建游戏窗口    480 x 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1>加载图像数据
bg = pygame.image.load("./images/background.png")

# 2>blit 绘制图像
screen.blit(bg, (0, 0))

# 3>update 更新屏幕显示
pygame.display.update()

while True:
    pass

# 游戏结束，卸载掉所有模块
pygame.quit()