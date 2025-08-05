class Person:
    def __init__(self,name_str,weight_str):
        self.name=name_str
        self.weight=weight_str

    def __str__(self):
        return f'我的名字是{self.name}，现在体重是{self.weight}kg'

    def running(self):
        print('跑步了')
        self.weight -= 0.5

    def eat(self):
        print('吃饭了')
        self.weight += 1

xiaoming=Person('小明',75)
xiaoming.running()
xiaoming.eat()
print(xiaoming)

xiao=Person('小美',45)
xiao.running()
xiao.eat()
print(xiao)