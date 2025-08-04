**字典：** 存储键值对

> dic['key']：查询指定key的值
> dic.get('key')：获取指定key的值
> dic['key']=value：增加一对键值对
> dic.pop('key')：删除指定的键值对
> len(dic)：查询字典中键值对的数量
> dic.update(temp_dic)：合并字典
> dic.clear()：清空字典

#### 字典的循环遍历
```
dic={'name':'zhang san',
     'sex':'male',
     'addr':'shang hai'}
     
for i in dic:
    print(i,dic[i])
```