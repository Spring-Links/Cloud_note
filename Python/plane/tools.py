import random
import pygame


SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
# 定时器
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):
        # 初始化父类
        super().__init__()
        self.image=pygame.image.load(image_name).convert_alpha()
        self.rect=self.image.get_rect()
        self.speed=speed


    def update(self):
        """垂直移动"""
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self,is_alt=False):
        super().__init__('./images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height

    # 重写update方法
    def update(self):
        super().update()
        # 判断y值是否超出屏幕高度
        if self.rect.y >= SCREEN_RECT.height:
            # 将y值设为屏幕高度的负值
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./images/enemy1.png')
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    def __init__(self):
        super().__init__('./images/me1.png',0)
        self.rect.centerx=SCREEN_RECT.centerx
        self.rect.bottom=SCREEN_RECT.bottom - 40

    def update(self):
        pass