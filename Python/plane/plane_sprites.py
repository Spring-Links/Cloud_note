import pygame

# 常量
# 屏幕大小
SCREEN_RECT=pygame.Rect(0,0,480,700)
# 帧率
FRAME_PER_SEC=60

class GameSprite(pygame.sprite.Sprite):
    """精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()
        self.image = pygame.image.load(image_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed


    def update(self):
        """垂直移动"""
        self.rect.y += self.speed


class BackGround(GameSprite):
    def  __init__(self,is_alt=False):
        super().__init__('./images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height