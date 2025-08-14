class Gun:
    def __init__(self,model):
        self.model=model
        self.bullet_count=0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <=0:
            print('子弹数量为零')
            return
        self.bullet_count-=1
        print(f'{self.model}-->Bone!,当前剩余子弹数量为{self.bullet_count}。')


class Soldier:
    def __init__(self,name_str):
        self.name=name_str
        self.gun=None

    def fire(self):
        if self.gun is None:
            print(f'{self.name}还没有武器')
            return

        print('go go go')

        self.gun.add_bullet(50)
        self.gun.shoot()


ak47=Gun('AK47')
arm=Soldier('许三多')
arm.gun=ak47
arm.fire()
print(arm.gun)

