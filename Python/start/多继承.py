class Father:
    def child(self):
        print('this is father')


class Mother:
    def demo(self):
        print('this is mother')

class Son(Father,Mother):
    pass


class ip(object):
    pass

son=Son()
son.child()
son.demo()
# print(Son.__mro__)
