```
import requests
from bs4 import BeautifulSoup
import os
import csv
import time
from dotenv import load_dotenv
import pymysql
```

```
#加载.env文件
load_dotenv(dotenv_path="./conf/mysql_con.env")

#定义一个列表
out_list=[]
```

```
#采集1-20页的数据
for num in range(1,21):
        # 请求的地址
        url=f"https://heb.anjuke.com/sale/nanganga/p{num}/"
        # 模拟用户请求
        header={"user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

        # 通过get方法采集url中的页面信息
        resp=requests.get(url=url,headers=header)
        # 打印页面信息
        # print(resp.text)
        # 使用漂亮汤解析html页面
        soup=BeautifulSoup(resp.text,"html.parser")
        # 遍历div标签，class_属性值
        for item in soup.find_all("div",class_="property-content"):
                introduction=item.find("div",class_="property-content-title").text
                house_type=item.find("div", class_="property-content-info").text.replace(" ", "").split()[0] #户型
                house_area=item.find("div", class_="property-content-info").text.replace(" ", "").split()[1] #面积
                house_towards=item.find("div", class_="property-content-info").text.replace(" ", "").split()[2] #朝向
                house_builtTime=item.find("div", class_="property-content-info").text.replace(" ", "").split()[-1] #建造时间
                house_floor=item.find("div", class_="property-content-info").text.replace(" ", "").split()[-2] #层数
                comm_name=item.find("div",class_="property-content-info property-content-info-comm").text.split()[0] #小区名称
                comm_address=item.find("div",class_="property-content-info property-content-info-comm").text.split()[-1] #小区地址
                house_price=item.find("div",class_="property-price").text.replace(" ","").split()[0] #房屋总价
                house_priceAve=item.find("div",class_="property-price").text.replace(" ","").split()[-1] #房屋均价
                # 将数据暂存至row_list
                row_list=[comm_name,comm_address,house_type,house_area,house_towards,house_floor,house_price,house_priceAve,introduction,house_builtTime]
                # 使用append方法将数据写入out_list中
                out_list.append(row_list)
                # print(house_builtTime)
        time.sleep(3)
```

```
# 数据库连接信息，将env文件中的数据库信息传入
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# 连接到MySQL数据库
conn = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    # 防止中文乱码
    charset='utf8mb4'
)

# 建立游标以执行mysql语句
cursor = conn.cursor()

# 插入数据的SQL语句
insert_query = """
INSERT INTO `test` 
(comm_name, comm_address, house_type, house_area, house_towards, house_floor, house_price, house_priceAve, introduction, house_builtTime) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# 批量插入数据
cursor.executemany(insert_query, out_list)

# 提交事务
conn.commit()

# 关闭连接
cursor.close()
conn.close()

print("数据成功写入数据库")
```