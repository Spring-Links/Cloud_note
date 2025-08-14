class A:
    def __init__(self):
        self.num1=100
        self.__num2=200

    def test(self):
        print(f'方法{self.num1},{self.__num2}')
        


class B(A):
    def demo(self):
        print(self.num1)
        self.test()

b=B()
b.demo()
print(b.num1)
