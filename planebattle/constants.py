# -*- coding:utf-8 -*-

"""
Desc: 常量

Author: ALion

Date: 2020/7/18 0:51
"""

import pygame

# 屏幕宽度
SCREEN_WIDTH = 420
# 屏幕高度
SCREEN_HEIGHT = 700

# 游戏每秒刷新次数
FRAME_PER_SECOND = 60

# 英雄飞机的移动速度
HERO_SPEED = 3

# 定时器-敌机
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定时器-子弹
CREATE_BULLET_EVENT = pygame.USEREVENT + 1