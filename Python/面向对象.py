# class Cat:
#     def eat(self):
#         print(f'{self.name}爱吃鱼')
#
#     def drink(self):
#         print(f'{self.name}要喝水')
#
# tom=Cat()
# tom.name='tom'
# tom.eat()
# tom.drink()
#
#
# lazy_cat=Cat()
# lazy_cat.name='lazy'
# lazy_cat.eat()
# lazy_cat.drink()

class Cat:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self.name+'爱吃鱼')

    def __str__(self):
        return '我是小猫 %s'% self.name

# 为创建的对象分配一块内存地址
# tom=Cat("Tom")
# tom.eat()

lazy_cat=Cat("lazy_cat ")
lazy_cat.eat()
print(lazy_cat)