class HouseItem:
    """"创建一个家具类"""
    def __init__(self,name_str,item_area_str):
        self.name=name_str
        self.area=item_area_str


class House:
    """创建一个房子类"""
    def __init__(self,house_type_str,house_area_str,name):
        self.house_type=house_type_str
        self.house_area=house_area_str
        self.free_area=house_area_str
        self.item_list=[]

    def __str__(self):
        return f'房子的户型是{self.house_type}，房子的面积是{self.house_area}，剩余面积{self.free_area}，家具有{self.item_list}'

    def add_item(self,item):
        if item.area > self.free_area:
            print(f'房间太小了，无法放下{item.name}')
            return

        self.item_list.append(item.name)
        self.free_area -= item.area



bed=HouseItem('席梦思',4)
table=HouseItem('桌子',8)

my_house=House('三室一厅',10)
my_house.add_item(table)
my_house.add_item(bed)
print(my_house)
