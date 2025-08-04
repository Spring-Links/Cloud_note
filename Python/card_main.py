import card_tools

while True:
    card_tools.show_menu()

    action=input('请输入您的操作：')
    print(f'您的操作是：{action}')

    if action in ['1','2','3']:
        if action=='1':
            card_tools.new_card()
        elif action=='2':
            card_tools.show_all()
        elif action=='3':
            card_tools.search_card()
        pass
    elif action=='0':
        print('再见！')
        break
    else:
        print('输入错误，请重新输入：')