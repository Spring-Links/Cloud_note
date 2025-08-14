class Women:
    def __init__(self,name):
        self.name=name
        self.__age=18


    def __secret(self):
        print(f'{self.name}的年龄是{self.__age}')

jack=Women('jack')
print(jack._Women__age)
jack._Women__secret()
