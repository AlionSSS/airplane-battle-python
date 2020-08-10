# -*- coding:utf-8 -*-

"""
Desc: 飞机大战的精灵对象

Author: ALion

Date: 2020/7/18 0:21
"""
import random
import pygame
from planebattle.constants import *


class GameSprite(pygame.sprite.Sprite):
    """
    精灵抽象基类
    """

    def __init__(self, image_name, speed=1, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    """
    游戏背景精灵
    """

    def __init__(self, is_alt=False, speed=1, *groups):
        image_name = "./../resources/images/background.png"
        super().__init__(image_name, speed, *groups)
        # 上面的第二张图片
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        self.rect.y += self.speed
        # 如果移出屏幕，将图像设置到上方
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = -self.rect.height


class HeroPlane(GameSprite):
    """
    英雄飞机精灵
    """

    def __init__(self, speed=1, *groups):
        image_name = "./../resources/images/me1.png"
        super().__init__(image_name, speed, *groups)
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.rect.x = (SCREEN_WIDTH - self.rect.width) >> 1
        self.x_speed = 0
        self.y_speed = 0
        # 子弹组
        self.bullet_group = pygame.sprite.Group()
        # 开火的开关
        self.fire_flag = False

    def update(self, *args):
        # 处理移动，边界检查
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
        half_width = self.rect.width >> 1
        if self.rect.x < -half_width:
            self.rect.x = -half_width
        elif self.rect.x > SCREEN_WIDTH - half_width:
            self.rect.x = SCREEN_WIDTH - half_width

    def fire(self):
        if self.fire_flag:
            # print("开始发射子弹...")
            x = self.rect.x + (self.rect.width >> 1)
            y = self.rect.y
            bullet = Bullet(x, y)
            self.bullet_group.add(bullet)


class EnemyPlane(GameSprite):
    """
    敌机精灵
    """

    def __init__(self, *groups):
        image_name = "./../resources/images/enemy1.png"
        speed = random.randint(1, 3)
        super().__init__(image_name, speed, *groups)
        # self.rect.y = -self.rect.height
        # 等效于上面
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            # 超出屏幕，销毁
            self.kill()

    def __del__(self):
        # print("__del__ %s" % self.rect)
        pass


class Bullet(GameSprite):
    """
    子弹
    """

    def __init__(self, x, y, speed=-1, *groups):
        image_name = "./../resources/images/bullet1.png"
        super().__init__(image_name, speed, *groups)
        self.rect.x = x - (self.rect.x >> 1)
        self.rect.y = y - self.rect.height

    def update(self, *args):
        super().update(*args)
        # 范围检查
        if self.rect.y < -self.rect.height:
            self.kill()

    def __del__(self):
        # print("__del__ %s" % self.rect)
        pass
