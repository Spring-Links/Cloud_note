class Game:

    top_score=0

    def __init__(self,player_name):
        self.player_name=player_name

    @staticmethod
    def show_help():
        print('--help')

    @classmethod
    def show_top_score(cls):
        print(f'历史记录：{cls.top_score}')

    def start_game(self):
        print(f'游戏开始，祝你好运{self.player_name}！')

Game.show_help()
Game.show_top_score()
jack=Game('jack')
jack.start_game()