class Animal:
    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


class Dog(Animal):
    def bark(self):
        print('汪汪叫')

class Cat(Animal):
    def catch(self):
        print('抓')

class XiaoTianQuan(Dog):
    def bark(self):
        print('不是汪汪叫')
        super().bark()
        print('fdjfljfld')
    def fly(self):
        print('飞')
        

boss=XiaoTianQuan()
# boss.eat()
# boss.drink()
# boss.run()
boss.bark()
boss.fly()
#
# miki=Cat()
# miki.catch()