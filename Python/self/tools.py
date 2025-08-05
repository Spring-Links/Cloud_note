def card_menu():
    # print('*'*50)
    title_str = 'Welcome use Card Manager'
    write_str = ' [1] Write'
    show_str = '[2] Show'
    select_str = '  [3] Select'
    exit_str = ' [0] exit '
    print(title_str.center(50,'='))
    print(write_str.center(48,' '))
    print(show_str.center(48,' '))
    print(select_str.center(48,' '))
    print(exit_str.center(48,' '))
    print('='*50)

card_lst=[
            {'name':'jack','sex':'male','age':'23'},
            {'name':'monika','sex':'female','age':'18'}
          ]
def card_write():
    print('*'*50)
    show='Write card'
    print(show.center(50,' '))
    name_str=(input('Name:'))
    sex_str=(input('Sex:'))
    age_str=(input('Age:'))
    card_dic={'name':name_str,'sex':sex_str,'age':age_str}
    card_lst.append(card_dic)
    print(card_dic)
    print(f'Success! Name is {name_str}')

def card_show():
    print('*'*50)
    show='Show cards'
    print(show.center(50,' '))
    for title in [f'Name\t\t\t\t Sex\t\t\t\t Age\t\t\t\t ']:
        print(title)
    for info in card_lst:
        print(f'{info['name']}\t\t\t\t {info['sex']}\t\t\t\t {info['age']}')


def card_select():
    print('*'*50)
    show='Select card'
    print(show.center(50,' '))
    select_name=input('Please input name: ')
    for result in card_lst:
        if result['name']==select_name:
            print(f'Name: {result['name']}\nSex: {result['sex']}\nAge: {result['age']}')
        break
    else:
        print('This card is not exist!')