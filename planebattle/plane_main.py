# -*- coding:utf-8 -*-

"""
Desc: Main入口

Author: ALion

Date: 2020/7/18 0:21
"""

import pygame

from planebattle.constants import *
from planebattle.plane_sprites import Background, HeroPlane, EnemyPlane


class PlaneGame(object):
    """
    飞机大战游戏主类
    """

    def __init__(self):
        print("PlaneGame 初始化")
        # 窗口
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 时钟
        self.clock = pygame.time.Clock()
        # 精灵
        self.__create_sprites()
        # 敌机定时事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 子弹定时事件
        pygame.time.set_timer(CREATE_BULLET_EVENT, 200)

    def __create_sprites(self):
        # 初始化背景精灵
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 初始化英雄飞机精灵
        self.hero = HeroPlane(3)
        self.hero_group = pygame.sprite.Group(self.hero)
        # 敌机
        self.enemy_group = pygame.sprite.Group()

    def __start__(self):
        print("PlaneGame 开始游戏")
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SECOND)  # 每秒执行60次
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        # 处理事件
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or \
                    event.type == pygame.QUIT:
                # 退出
                self.__game_over()
            elif event.type == pygame.KEYDOWN:  # 按键按下
                # 处理移动
                if event.key == pygame.K_LEFT:
                    self.hero.x_speed = -self.hero.speed
                elif event.key == pygame.K_RIGHT:
                    self.hero.x_speed = self.hero.speed
                elif event.key == pygame.K_UP:
                    self.hero.y_speed = -self.hero.speed
                elif event.key == pygame.K_DOWN:
                    self.hero.y_speed = self.hero.speed
                elif event.key == pygame.K_LCTRL:
                    # 允许开火
                    self.hero.fire_flag = True
            elif event.type == pygame.KEYUP:  # 按键释放
                # 停止移动
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.hero.x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.hero.y_speed = 0
                elif event.key == pygame.K_LCTRL:
                    # 禁止开火
                    self.hero.fire_flag = False
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                enemy = EnemyPlane()
                self.enemy_group.add(enemy)
            elif event.type == CREATE_BULLET_EVENT:
                # 发射子弹
                self.hero.fire()

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # 敌机摧毁英雄飞机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 英雄飞机牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 绘制背景
        self.back_group.update()
        self.back_group.draw(self.screen)
        # 绘制敌机
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        # 绘制Hero飞机
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("PlaneGame 游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    pygame.init()
    try:
        game = PlaneGame()
        game.__start__()
    finally:
        pygame.quit()
        exit()
