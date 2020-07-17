# -*- coding:utf-8 -*-

"""
Desc: 飞机大战的精灵对象

Author: ALion

Date: 2020/7/18 0:21
"""
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
        self.x_offset = 0
        self.y_offset = 0

    def update(self, *args):
        # 处理移动，边界检查
        self.rect.x += self.x_offset
        self.rect.y += self.y_offset
        if self.rect.y < -self.rect.height:
            self.rect.y = -self.rect.height
        elif self.rect.y > SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT
        if self.rect.x < -self.rect.width:
            self.rect.x = -self.rect.width
        elif self.rect.x > SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH
