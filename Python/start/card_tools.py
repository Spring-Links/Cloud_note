def show_menu():
    """显示菜单"""
    print('*'*50)
    print('欢迎使用【名片管理系统】V 1.0\n')
    print('1. 新增名片')
    print('2. 显示全部')
    print('3. 查询名片\n')
    print('0. 退出系统')
    print('*'*50)

card_lst=[{'name':'jack',
              'phone':'911',
              'email':'jack@email.com',
              'addr':'shang hai'
              },
          {'name': 'monika',
           'phone': '911',
           'email': 'jack@email.com',
           'addr': 'shang hai'
           }
          ]

def new_card():
    print('-'*50)
    print('新增名片')
    name_str=input('请输入姓名：')
    phone_str=input('请输入电话：')
    email_str=input('请输入邮箱：')
    addr_str=input('请输入地址：')

    card_dic={'name':name_str,
              'phone':phone_str,
              'email':email_str,
              'addr':addr_str
              }
    card_lst.append(card_dic)
    print(card_lst)
    print(f'已经添加{name_str}的信息。')

def show_all():
    print('-' * 50)
    print('显示所有名片')
    if len(card_lst)==0:
        print('没有记录，请添加名片')
        return
    for title in ['姓名','电话','邮箱','地址']:
        print(title,end='\t\t')
    print('')
    print('='*50)
    for data in card_lst:
        print(f'{data['name']}\t\t{data['phone']}\t\t{data['email']}\t\t{data['addr']}')

def search_card():
    print('-' * 50)
    print('搜索名片')
    search_name=input('请输入要搜索的姓名：')
    for data in card_lst:
        if data['name']==search_name:
            # for title in ['姓名', '电话', '邮箱', '地址']:
            #     print(title, end='\t\t')
            # print('\n')
            # print('=' * 50)
            for data in card_lst:
                print(f'{data['name']}\t\t{data['phone']}\t\t{data['email']}\t\t{data['addr']}')
            deal_card(data)
            break
    else:
        print('查无此人')

def deal_card(find_dic):
    print(find_dic)
    action_str=input('请选择要执行的操作 '
                     '[1] 修改 [2] 删除 [0] 返回上一级\n待输入：')
    if action_str in ['1','2']:
        if action_str=='1':
            find_dic['name']=input_card_info(find_dic['name'],'姓名：')
            find_dic['phone']=input_card_info(find_dic['phone'],'电话：')
            find_dic['email']=input_card_info(find_dic['email'],'邮箱：')
            find_dic['addr']=input_card_info(find_dic['addr'],'地址：')
            print('修改名片')
        elif action_str=='2':
            card_lst.remove(find_dic)
            print('删除名片')


def input_card_info(dic_value,tip_mess):
    result_str=input(tip_mess)
    if len(result_str)>0:
        return result_str
    else:
        return dic_value