#### 软件源
> https://mirrors.aliyun.com/centos/8-stream/BaseOS/x86_64/os/
#### yum源
1.进入配置文件删除所有 .repo文件,使用ls查看是否正确删除
> cd /etc/yum.repos.d/
> rm *.repo
> ls

2.下载阿里云的repo文件
> curl -o /etc/yum.repo.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo

运行yum makecache生成缓存
> yum makecache

#### 设置静态ip
1.修改网卡配置文件
> vim /etc/sysconfig/network-scripts/ifcfg-ens160

2.更改配置文件
>BOOTPROTO=dhcp→BOOTPROTO=static
>ONBOOT=yes

3.添加静态ip及相关信息
>IPADDR=""   #想要设置的静态ip
NETMASK="255.255.255.0"   #子网掩码
GATEWAY=""   #网关地址
DNS1=""   #dns域名解析

4.重启网卡
>nmcli connection down ens160 #停用网卡
>nmcli connection up ens160 #激活网卡

5.查看ip是否更改成功
>ifconfig