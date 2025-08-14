import pygame
from plane_sprites import *

class PlanGame(object):
    def __init__(self):
        print('游戏初始化...')
        # 创建游戏窗口
        self.screen=pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock=pygame.time.Clock()
        # 调用私有方法
        self.__create_sprites()
    # 创建精灵
    def __create_sprites(self):
        bg1=BackGround()
        bg2=BackGround(True)
        self.back_group=pygame.sprite.Group(bg1,bg2)
        pass

    def start_game(self):
        print('游戏开始')
        while True:
            # 设置刷新率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                PlanGame.__game_over()

    def __check_collide(self):
        pass
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

if __name__ == '__main__':

    game=PlanGame()
    game.start_game()