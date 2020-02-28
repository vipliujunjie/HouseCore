import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1、创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2、创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3、调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 200)
        # 设置定时器事件 - 子弹 0.5s
        pygame.time.set_timer(HERO_FIRE_EVENT, 200)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        enemy1 = Enemy()
        self.enemy_group = pygame.sprite.Group(enemy1)

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")

        while True:
            # 1、设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新/绘制精灵组
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()
            # pygame.event.get()    这里监听会报错

    def __event_handler(self):  # 事件监听
        for event in pygame.event.get():
            # 判断事件类型是否是退出事件 - 是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 开关按键
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("退出")
                self.__game_over()

        # 使用键盘提供的方法获取键盘按键 - 按键元组    点动
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_LEFT]:
            self.hero.speed = 10

        elif keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = -10

        elif keys_pressed[pygame.K_UP]:
            self.hero.rect.y -= 10

        elif keys_pressed[pygame.K_DOWN]:
            self.hero.rect.y -= -10

        else:
            self.hero.speed = 0

    def __check_collide(self):   # 检测碰撞
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容
        if len(enemies) > 0:

            # 让英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):  # 更新精灵
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()   # 更新敌机位置
        self.enemy_group.draw(self.screen)  # 绘制敌机精灵

        self.hero_group.update()    # 更新英雄位置
        self.hero_group.draw(self.screen)   # 绘制英雄

        self.hero.bullets.update()      # 更新子弹位置
        self.hero.bullets.draw(self.screen)     # 绘制子弹

    @staticmethod
    def __game_over():
        print("游戏结束！")
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()

