**下载repo源**
`rpm -Uvh https://repo.zabbix.com/zabbix/6.0/rhel/8/x86_64/zabbix-release-latest-6.0.el8.noarch.rpm`

**清除缓存**
`dnf clean all`

**安装agent**
`dnf install zabbix-agent`

**启动agent**
`systemctl restart zabbix-agent`

**指定server的地址**
`vim /etc/zabbix/zabbix_agentd.conf`

**启动 zabbix-agent**
`systemctl restart zabbix-agent`


