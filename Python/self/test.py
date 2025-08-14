# card_lst=[
#             {'name':'jack','sex':'male','age':'23'},
#             {'name':'monika','sex':'female','age':'18'}
#           ]
#
# print(id(card_lst))
# input_name=input('name:')
# for result in card_lst:
#     if result['name']==input_name:
#         print(f'Name: {result['name']}\nSex: {result['sex']}\nAge: {result['age']}')

# count=input('need a count')
# count=int(count)
# if count==1:
#     print('one')
# elif count==2:
#     print('two')
# elif count==3:
#     print('three')
# else:
#     print('not found')

# while True:
#     count = input("need a count: ")  # 提示用户输入
#     try:
#         num = int(count)  # 尝试转为整数
#         print('success')
#         break  # 成功则退出循环
#     except ValueError:  # 捕获转换失败异常
#         print("输入无效，必须为整数！请重试。")



# class Person:   #定义一个Person类
#     def __init__(self,name,age):   #对类进行初始化，初始化时就可以进行属性定义，如name、age
#         self.name=name
#         self.age=age
#
#     def introduction(self):   #定义一个方法
#         print(f'{self.name}的年龄是{self.age}')
#
# jack=Person('jack',18)   #用类创建一个对象jack
# jack.introduction()   #通过创建的对象jack调用introduction方法

