```
调用函数、方法时需要()，而关键字后不需要()
函数封装了独立的功能，可以直接调用。
方法和函数类似都是封装了独立的功能，
但方法需要通过对象来调用
```
#### 列表元素的增删改查及排序
> lst.index('data)：查看data所在的索引位置

> lst['data_index']='new_data'：修改指定索引的数据

> lst.append('new_data')：末尾插入新数据

> lst.insert('index','new_data')：在指定的索引位置插入数据

> lst.expend('other_list')：将其他列表以独立的列表追加到当前列表

> lst.remove('data')：将data进行删除

> lst.pop('data_index')：将指定索引的数据删除，默认删除最后一个

> lst.clear()：将列表内容进行清空

> del lst['data_index']：将指定的index数据删除（将变量从内存中删除）

> lst.len()：统计元素个数

> lst.count('data')：统计data出现的次数

> lst.sort()：升序

> lst.sort(reverse=True)：降序

> lst.reverse()：反转

#### 列表的循环遍历

```
lst=['张三','李四','王五','赵六','孙七']

for i in lst:
    print(i)
```