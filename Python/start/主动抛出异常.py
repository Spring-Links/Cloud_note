def input_password():
    passwd=input('请输入密码：')
    if len(passwd) >= 8:
        return passwd
    # ex=Exception('密码长度小于8.')
    # raise ex
    print('密码长度不够')
# try:
#     print(input_password())
#
# except Exception as result:
#     print(result)
print(input_password())