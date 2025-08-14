**环境准备**
- centos8
- mysql_8.0
- nginx_1.14.1
- zabbix_6.0

**下载repo源**
`rpm -Uvh https://repo.zabbix.com/zabbix/6.0/rhel/8/x86_64/zabbix-release-latest-6.0.el8.noarch.rpm`

**清除缓存**
`dnf clean all`

**安装zabbix服务组件**
```
dnf install zabbix-server-mysql zabbix-web-mysql zabbix-nginx-conf zabbix-sql-scripts zabbix-selinux-policy zabbix-agent
```

**创建zabbix用户及数据库**
```
-- MySQL
create database zabbix character set utf8mb4 collate utf8mb4_bin;
create user zabbix@localhost identified by 'password';
grant all privileges on zabbix.* to zabbix@localhost;
set global log_bin_trust_function_creators = 1;
quit;
```

**导入zabbix所需表**
```
zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix

-- MySQL
set global log_bin_trust_function_creators = 0;
quit;
```

**为zabbix server配置数据库**
```
vim /etc/zabbix/zabbix_server.conf
DBPassword=password
```

**配置前端php**
```
vim /etc/nginx/conf.d/zabbix.conf  # uncomment and set 'listen' and 'server_name' directives.
listen 8080;
server_name example.com;
```

**启动server和agent进程**
`systemctl restart zabbix-server zabbix-agent nginx php-fpm`

**设置开机自启**
`systemctl enable zabbix-server zabbix-agent nginx php-fpm`


<!-- sudo firewall-cmd --add-port=80/tcp --permanent


max_allowed_packet = 64M


explicit_defaults_for_timestamp=true

rm -rf /var/lib/mysql/* -->

