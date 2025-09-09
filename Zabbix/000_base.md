**监控：**
- **硬件信息：** 磁盘、raid状态、温度、风扇转速、机房温度、湿度
- **系统信息：** cpu、内存(swap、buffer、cache)、磁盘(io、使用率、inode)、负载、网络(in\out)
- **服务信息：** 服务状态、端口、进程、特定信息
- **业务信息：** 应用程序代码是否有问题

**agent日志文件**
`cat /var/log/zabbix/zabbix_agentd.log`

==服务端向客户端请求数据==

**在server端查看是否能获取agent端信息**
- **在服务端安装zabbix_get**
`yum install zabbix-get.x86_64 `

- **测试服务器是否能获取客户端数据**
`zabbix_get -s 192.168.174.125 -p 10050 -k system.hostname`

**修复乱码**
- **使用微软雅黑等通用字体替换zabbix默认字体**
`/usr/share/zabbix/assets/fonts/graphfont.ttf`

**自定义模板**

- **检测agent机器上是否有root远程登陆**
```
-- agent端

1. 查看agent配置文件的Include对应的值
cat /etc/zabbix/zabbix_agentd.conf

2. 在zabbix_agentd.d目录下创建*.conf配置文件
vim /etc/zabbix/zabbix_agentd.d/*.conf


conf文件格式
UserParameter=key_name,value
示例：UserParameter=root.login,who | awk '$1=="root"' | wc -l

重启agent服务
systemctl restart agent
```

```
-- server端

在服务端使用zabbix_get方法测试
zabbix_get -s node07 -k root.login
```

**监控项：** 服务端向客户端获取数据的方式
- **名称：** 监控项的名称
- **键值：** 
- **更新间隔：** 数据的更新时间
- **历史数据保留期：** 数据保留的时长
- **趋势存储时间：** 截取历史数据的值绘制的趋势图，能反映数据的大概走势
- **测试**
  - **获取值：** 反应zabbix_get是否可用
  - **获取值并进行测试：** 反应php页面的监控项是否可用

**触发器：** 判断监控项中获取的值是否触发告警
- **表达式：** 方法(/主机名/key_name)>=2
  - **例如：** last(/node07/root.login)>=2
- **事件迭代成功**
  - **恢复表达式：** 判断问题恢复的条件
    - **例如：** last(/node07/root.login)<2

**分发自定义的监控项**
- **简介：**
``在一台机器中自定义一个监控项、触发器、图形，
再新建一个模板文件，将自定义的项都添加进该模板文件，
在想要监控的其他服务器中将自定义的模板文件与其绑定，
将linux中的conf文件进行相应的分发，并在对应的服务器中重启agent服务
``

**自动发现**
客户端配置agent的conf文件，将server的地址指向服务端ip地址,在web页面配置自动发现规则和自动发现动作

**自动注册：**
```
在客户端配置agent的conf文件
将Server的地址指向服务端ip地址
将ServerActiv地址也指向serverip地址
填写HostnameItem=system.hostname
填写HostMetadataItem=system.uname
在web上配置自动注册动作
```