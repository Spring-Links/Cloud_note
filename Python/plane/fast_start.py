import pygame
from plane_sprites import *

# 初始化
pygame.init()

# 创建一个主窗口
screen=pygame.display.set_mode((480,700))

# 加载背景资源
bg=pygame.image.load('./images/background.png')
# 将背景绘制到主窗口
screen.blit(bg,(0,0))

# 加载主角
hero=pygame.image.load('./images/me1.png')
screen.blit(hero,(200,500))


# 刷新屏幕
pygame.display.update()

clock=pygame.time.Clock()

hero_rect=pygame.Rect(200,500,102,126)
# 游戏循环 ->意味着游戏正式开始

enemy=GameSprite('./images/enemy1.png')
enemy1=GameSprite('./images/enemy1.png',2)

enemy_group=pygame.sprite.Group(enemy,enemy1)







while True:
    # 刷新：60
    clock.tick(60)
    # 捕获事件
    event_list=pygame.event.get()
    for event in event_list:
        if event.type==pygame.QUIT:
            print('退出游戏')
            # 卸载模块
            pygame.quit()
            # 终止程序
            exit()

    # 每秒移动的像素
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y=700
    # 重新绘制背景和英雄
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)


    # 更新屏幕
    pygame.display.update()

