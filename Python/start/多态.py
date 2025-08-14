class Cat:
    def __init__(self,name):
        self.name=name

    def game(self):
        print('普通的玩耍')

class Dog:
    def __init__(self,name):
        self.name=name

    def game(self):
        print('普通的玩耍')



class XiaoTianQuan(Dog):
    def game(self):
        print('神一样的玩耍')

class Person:
    def __init__(self,name):
        self.name=name

    def game_with_dog(self,dog):
        print(f'{self.name}和{dog.name}玩耍')
        dog.game()



gold=Dog('wangcai')
cat=Cat('cat')
xiaoming=Person('xiaoming')
xiaoming.game_with_dog(gold)
xiaoming.game_with_dog(cat)
