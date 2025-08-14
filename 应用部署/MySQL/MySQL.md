## 离线安装
**准备工作**
1.系统：CentOS 8
2.mysql安装包：mysql-8.0.40-1.el8.x86_64.rpm-bundle.tar
****
**卸载mariadb**
1.查看系统中是否有mariadb
`rpm -qa | grep mariadb`
- rpm -qa：查询所有已安装的rpm包
  
2.如果有mariadb则执行卸载
`rpm -e --nodeps 安装包`
- -e：erase.清除、删除
- --nodeps：忽略依赖关系检查

**新建文件夹并上传解压mysql压缩包**
1.新建mysql文件夹
`cd /usr/local`
`mkdir mysql`
2.使用xftp将压缩包上传至/usr/local/mysql中
3.解压缩压缩包
`tar -xvf mysql-8.0.40-1.el8.x86_64.rpm-bundle.tar`

**安装初始化并授权防火墙**
1.安装mysql
```
rpm -ivh --nodeps --force mysql-community-common-8.0.40-1.el8.x86_64.rpm
rpm -ivh --nodeps --force mysql-community-libs-8.0.40-1.el8.x86_64.rpm
rpm -ivh --nodeps --force mysql-community-client-8.0.40-1.el8.x86_64.rpm
rpm -ivh --nodeps --force mysql-community-server-8.0.40-1.el8.x86_64.rpm
```
- -i：install
- -v：verbose.输出详细信息，使用户能看到更详细的安装过程
- -h：hashes.以进度条(#)形式显示
- --nodeps：忽略依赖检查
- --force：强制安装，允许覆盖相同名称和版本的软件包
- common：提供了mysql软件包都想要的公共文件
- libs：绝大部分访问mysql的应用程序都要依赖该库
- client：用于管理操作mysql数据库
- server：包含运行mysql服务所需的所有文件和可执行文件(如mysqld)

2.初始化mysql
`mysqld --initialize`
- mysqld --initialize：用于初次安装mysql时创建mysql数据目录并生成一个临时的root密码 (/var/log/mysqld.log)

3.修改所属权和自启
`chown mysql:mysql /var/lib/mysql -R`
- chown：更改文件所属权
- mysql:mysql：将文件所有者和所属组都更改为mysql
- var/lib/mysql -R：对该目录下的所属权进行递归更改

`systemctl start mysqld.service` 启动mysql服务

`systemctl enable mysqld` 将服务自启开启

**查看密码并修改密码和时区**
1.查看密码
`cat /var/log/mysqld.log | grep password`

2.修改密码
`mysql -uroot -p` 登录mysql
`alter user 'root'@'localhost' identified with mysql_native_password by 'root';` 将密码修改为root
alter user 'root'@'localhost' identified with caching_sha2_password by 'password';
skip-grant-tables

3.修改时区
`set global time_zone='+8:00';` 将时区修改为中国标准时间.UTC+8


==关于mysql5.7文件缺失的问题==
**缺失文件**
- libncurses.so.5
- libtinfo.so.5

**解决办法**
- 创建软链接
```
ln -s /usr/lib64/libtinfo.so.6 /usr/lib64/libtinfo.so.5
ln -s /usr/lib64/libncurses.so.6 /usr/lib64/libncurses.so.5
```

mysql> set global validate_password_policy=0;
