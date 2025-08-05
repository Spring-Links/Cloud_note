# def intro(name,sex=True):
#
#     sex_str='male'
#     if not sex:
#         sex_str='female'
#     print(f'{name} is {sex_str}')
#
# intro(45)
# intro(45,False)
#
# def line(num,*nums,**person):
#     print(num)
#     print(nums)
#     print(person)
#
# line(1,2,3,4, name='xiaoming')

# def sum_num(*args):
#     num=0
#     print(args)
#     for i in args:
#         num += i
#     return num
#
# result=sum_num(1,2,3,4,5)
# print(result)

# def demo(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# num=(1,2,3,4)
# num1={"name":"jack","sex":"male"}
# demo(*num,**num1)

def demo(num):
    print(num)
    if num==1:
        return
    demo(num-1)
demo(2)

