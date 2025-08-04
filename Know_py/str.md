> len(str1)：统计字符串长度

> str1.count('data')：统计data出现的次数

> str1.index('data')：查看data的索引位置

> str1.isspace()：判断空白字符

> srt1.isdecimal()：只能判断是否为纯整数(不包含浮点数、负
数等)

> srt1.isdigit()：在isdecimal的基础上增加了判断unicode

> srt1.isnumeric()：在isdigit的基础上增加了判断中文数字

> srt1.startswith('sta')：判断是否为sta开始，区分大小写

> srt1.endswith('ed')：判断是否为ed结束

> srt1.find('data')：查找指定字符串的索引位置，与str1.index相比，
当查找不到指定字符串时不会报错

> srt1.replace('old_data','new_data')：替换旧的数据，会返回一个新的字符串
而不去修改原有的字符串

> srt1.ljust(10," ")：文本左对齐

> srt1.rjust(10," ")：文本右对齐

> srt1.center(10," ")：文本居中

> str1.lstrip()：去除左边的空白字符

> str1.rstrip()：去除右边的空白字符

> str1.strip()：去除字符串左右两边的空白字符串

> str1.split('seq',num)：将大段字符串分割为列表,seq指定分割符，num则指定分割num+1个子字符串

> "seq".join(list_str)：将列表以seq为连接符转为字符串

> str1['开始':'结束':'步长']：字符串切片
> 