**查看系统版本**
`cat /etc/redhat-release`

**解析主机名**
`vim /etc/hosts`

**同步时间**
`systemctl start chronyd`

**关闭防火墙**
`systemctl stop firewalld`

**禁用iptables**
`systemctl stop iptables`

**禁用selinux**
`setenforce 0/vim /etc/selinux/config`

**禁用swap分区（注释swap所在行）**
`vim /etc/fstab`

**修改linux内核参数**
```
vim /etc/sysctl.d/kubernetes.conf
net.brige.brige-nf-call-ip6tables = 1
net.brige.brige-nf-call-iptables = 1
net.ipv4.ip_forward = 1

sysctl -p
```

**加载网桥过滤模块**
`modprobe br_netfilter`

**查看模块是否加载成功**
`lsmod | grep br_netfilter`

**安装配置ipvsadm ipset**
`yum install ipvsadm ipset -y`

**添加需要加载的模块**
```
vim /etc/sysconfig/modules/ipvs.modules
#!/bin/bash
modprobe -- ip_vs
modprobe -- ip_vs_rr
modprobe -- ip_vs_wrr
modprobe -- ip_vs_sh
modprobe -- nf_conntrack_ipv4
```

**为文件添加执行权限**
`chmod +x /etc/sysconfig/modules/ipvs.modules `

**执行脚本文件**
`/bin/bash /etc/sysconfig/modules/ipvs.modules`

**查看模块是否加载成功**
`lsmod | grep -e ip_vs -e nf_conntrack_ipv4`

**重启服务器，并检查设置是否生效**
```
reboot
getenforce
free -m
```

**安装特定版本docker**
