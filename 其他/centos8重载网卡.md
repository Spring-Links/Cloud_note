nmcli connection reloas
nmcli connection up ens160

添加默认网卡：sudo ip route add default via 192.168.174.2 dev ens160

设置yum源
rm -rf /etc/yum.repos.d/*.repo
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
yum makecache