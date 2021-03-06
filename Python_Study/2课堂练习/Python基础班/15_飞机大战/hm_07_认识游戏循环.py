import pygame
import time
# 使用pygame模块必须先调用pygame.init()来加载其他模块
pygame.init()

# 创建游戏窗口    480 x 700
screen = pygame.display.set_mode((480, 700))

# 绘制 -背景图像
# 1>加载图像数据
bg = pygame.image.load("./images/background.png")

# 2>blit 绘制图像
screen.blit(bg, (0, 0))

# 3>update 更新屏幕显示
# pygame.display.update()
# pygame.event.get()  # ⚠️必须加这行才能显示

# 绘制 -英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (189, 500))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()
pygame.event.get()  # ⚠️必须加这行才能显示


# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环  ->意味着游戏的正式开始
i = 0

while True:
    clock.tick(60)
    print(i)
    i += 1
    # pygame.event.get()

# 游戏结束，卸载掉所有模块
pygame.quit()
