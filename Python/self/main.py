import tools

while True:
    tools.card_menu()
    function_num = input('Please input your count：')
    print(f'Your count is: {function_num}')
    if function_num in ['1','2','3']:
        if function_num=='1':
            tools.card_write()
        if function_num=='2':
            tools.card_show()
        if function_num=='3':
            tools.card_select()
    elif function_num=='0':
        break
    else:
        print('Error! check your count.')

    