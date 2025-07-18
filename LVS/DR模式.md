**准备工作**
==关闭负载均衡节点服务器的防火墙==
- **服务器**
  - ds：192.168.174.150
  - rs01：192.168.174.124
  - rs02：192.168.174.125
- **VIP：** 192.168.174.200

**配置DS**
```
-- 关闭防火墙
systemctl stop firewalld
-- 开启ip转发，因为ds需要将请求发给rs
echo 1 > /proc/sys/net/ipv4/ip_forward
-- 将vip绑定到ens160上，并创建一个虚拟子接口ens160:0
ip addr add 192.168.174.200/32 dev ens160 label ens160:0
-- 开启创建的虚拟接口ens160:0
ip link set ens160:0 up
-- 添加一条路由规则：将所有目标为vip的流量都通过虚拟接口ens160:0
ip route add 192.168.174.200 dev ens160:0
-- 清除所有ipvs规则
ipvsadm -C
-- 创建虚拟服务：-A： 添加一个虚拟服务器 -t：指定虚拟服务为tcp服务 -s：指定调度算法
ipvsadm -A -t 192.168.174.200:80 -s rr
-- -a：为虚拟服务添加一个rs -t：该虚拟服务为tcp服务 -r：vip转发到rip -g：使用DR模式（网关模式）
ipvsadm -a -t 192.168.174.200:80 -r 192.168.174.124:80 -g
ipvsadm -a -t 192.168.174.200:80 -r 192.168.174.125:80 -g
-- 以数字格式显示当前的ipvs规则
ipvsadm -Ln
```

**配置RS**
```
systemctl stop firewalld
setenforce 0
yum install httpd -y
-- 将vip绑定到lo上，并创建一个虚拟子接口lo:0
ip addr add 192.168.174.200/32 dev lo label lo:0
-- 开启新创建的虚拟接口lo:0
ip link set lo:0 up
-- 添加路由规则，所有目标为vip的流量进入虚拟接口lo:0
ip route add 192.168.174.200 dev lo:0
-- 只响应目标ip是本机入网地址的arp请求
echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore
-- 优先与目标ip在同一子网的地址
echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce
-- 对lo应用与全局相同的arp忽略规则
echo 1 > /proc/sys/net/ipv4/conf/lo/arp_ignore
-- 对lo应用与全局相同的arp通告规则
echo 2 > /proc/sys/net/ipv4/conf/lo/arp_announce
echo "<h1>124</h1>" > /var/www/html/index.html
systemctl restart httpd
```

**测试**
在物理机中访问192.168.174.200，使用无痕窗口访问会看到192.168.174.124和192.168.174.125两个进行轮询