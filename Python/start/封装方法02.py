class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        return f'{self.name},占地{self.area}平米'


class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.item_list=[]

    def __str__(self):
        return (f'房子户型是{self.house_type}，总面积{self.area}平米，'
                f'面积剩余{self.free_area}平米，家具有{self.item_list}')

    def add_item(self,item):
        print(f'要添加家具{item.name}')

        if item.area > self.free_area:
            print(f'{item.name}占地面积太大了')
            return

        self.item_list.append(item.name)
        self.free_area -= item.area
        print(f'现在房子剩余面积{self.free_area}平米')


bed=HouseItem('席梦思',4)
chest=HouseItem('衣柜',2)
table=HouseItem('餐桌',1.5)
print(bed)
print(chest)
print(table)

my_home=House('两室一厅',6)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)