import pygame
from tools import *

class PlanGame(object):

    def __init__(self):
        # 创建窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        self.clock=pygame.time.Clock()
        self.__create_sprite()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)


    # 开始游戏
    def start_game(self):
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    # 游戏结束
    def over_game(self):
        pass

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == CREATE_ENEMY_EVENT:
                enemy=Enemy()
                self.enemy_group.add(enemy)

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            #     print('down')

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_DOWN]:
            print('down')

    # 创建精灵
    def __create_sprite(self):
        bg1=BackGround()
        bg2=BackGround(True)
        self.back_group = pygame.sprite.Group((bg1,bg2))
        self.enemy_group = pygame.sprite.Group()
        self.hero=Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 更新精灵
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)

    # 检测碰撞
    def __check_collide(self):
        pass


# 主程序入口
if __name__ == '__main__':
    game=PlanGame()
    game.start_game()