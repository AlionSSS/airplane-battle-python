# -*- coding:utf-8 -*-

"""
Desc: Main 入口

Author: ALion

Date: 2020/7/14 23:12
"""
import pygame


def run():
    # 创建游戏窗口 480 * 700
    screen = pygame.display.set_mode((480, 700))

    # 加载背景图
    bg_img = pygame.image.load("./../resources/images/background.png")

    # 加载Hero飞机图像
    hero_img = pygame.image.load("./../resources/images/me1.png")
    # 获取宽高，修正偏移
    _, _, width, height = hero_img.get_rect()
    x = 240 - (width >> 1)
    y = 700 - height

    x_offset = 0
    y_offset = 0
    speed = 3

    # 时钟
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)  # 每秒执行60次

        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                # 退出
                return
            elif event.type == pygame.KEYDOWN:  # 按键按下
                # 处理移动
                if event.key == pygame.K_LEFT:
                    x_offset = -speed
                elif event.key == pygame.K_RIGHT:
                    x_offset = speed
                elif event.key == pygame.K_UP:
                    y_offset = -speed
                elif event.key == pygame.K_DOWN:
                    y_offset = speed
            elif event.type == pygame.KEYUP:  # 按键释放
                # 停止移动
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_offset = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_offset = 0

        # 绘制背景
        screen.blit(bg_img, (0, 0))

        # 绘制Hero飞机
        # 处理移动，边界检查
        x += x_offset
        y += y_offset
        if y < -height:
            y = -height
        elif y > 700:
            y = 700
        if x < -width:
            x = -width
        elif x > 700 + width:
            x = 700 + width
        screen.blit(hero_img, (x, y))

        # 更新界面
        pygame.display.update()


if __name__ == '__main__':
    # hero = pygame.Rect(0, 0, 100, 100)
    # print("原点 %d, %d" % (hero.x, hero.y))
    # print("尺寸 %d, %d" % (hero.width, hero.height))
    # print(f"原点({hero.x}, {hero.y}), 尺寸({hero.width}, {hero.height})")

    pygame.init()

    try:
        run()
    finally:
        pygame.quit()
