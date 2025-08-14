try:
    num=int(input('请输入一个整数：'))
    re = 8/num
    print(re)

except ValueError:
    print('请输入一个正确的整数')

except Exception as result:
    print(f'未知错误：{result}')

else:
    print(f'恭喜你输入正确，你输入的是{num}，它除以8了，所以结果是{re}')

finally:
    print('结束')

print('*'*50)