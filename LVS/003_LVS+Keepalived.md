**准备工作**
==关闭所有服务器的防火墙和selinux==
- **服务器**
  - ds01：192.168.174.150
  - ds02：192.168.174.160
  - rs01：192.168.174.124
  - rs02：192.168.174.125
- **VIP：** 192.168.174.200
- **其他说明：** 各个服务器均已完成DR模式下的操作，如配置ds和rs。详见/note/LVS/DR模式.md

**配置DS**
```
-- MASTER
yum install keepalived -y
vim /etc/keepalived/keepalived.conf
systemctl restart keepalived
```
```
-- BACKUP
systemctl stop firewalld
setenforce 0
yum install ipvsadm keepalived -y
vim /etc/keepalived/keepalived.conf
```

**测试**
在物理机上访问192.168.174.200，正常访问后关闭master上的keepalived服务，在backup节点上利用`ip addr show ens160`或者`ipvsadm -Ln`观察vip是否已经漂移到backup节点上，在物理机上重新访问139.168.174.200看看网页是否正常