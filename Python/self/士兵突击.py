class Gun:
    def __init__(self,model,bullet_count):
        self.model=model
        self.bullet_count=bullet_count

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print(f'shoot!!!{self.bullet_count}')
        else:
            print('子弹数量不够')


class Solider:
    def __init__(self,name):
        self.name=name
        self.gun=None

    def fire(self):
        if self.gun is None:
            print('无武器')
            return
        else:
            print('go go go')



ak47=Gun('AK47',10)
ak47.shoot()


