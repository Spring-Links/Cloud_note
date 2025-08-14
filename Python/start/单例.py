# class MusicPlayer:
#     def __new__(cls, *args, **kwargs):
#         print('调用了new方法')
#         instance=super().__new__(cls)
#         return instance
#
#     def __init__(self):
#         print('初始化完成')
#
#
# player=MusicPlayer()
# print(player)

class MusicPlayer():
    instance=None
    init_flag=False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance

    def __init__(self):

        if MusicPlayer.init_flag:
            return
        print('success')

        MusicPlayer.init_flag=True



player1=MusicPlayer()
print(player1)
player2=MusicPlayer()
print(player2)