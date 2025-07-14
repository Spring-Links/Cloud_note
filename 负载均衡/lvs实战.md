准备工作：
    三台服务器：192.168.174.124（负载均衡）192.168.174.166（网站1）192.168.174.167（网站2）
    服务器关闭firewall、selinux

1.关闭firewall
systemctl stop firewalld

2.关闭selinux
setenforce 0
getenforce

3.在负载均衡上安装ipvsadm，添加vip
yum -y install ipvsadm
ip addr add dev ens160 192.168.174.120/32

4.创建规则文件并启动ipvsadm
ipvsadm --save > /etc/sysconfig/ipvsadm
systemctl start ipvsadm

5.定义规则
    添加虚拟服务器
        ipvsadm -A -t 192.168.174.120:80 -s rr
    在虚拟服务器中添加web服务器地址
        ipvsadm -a -t 192.168.174.120:80 -r 192.168.174.166 -g
        ipvsadm -a -t 192.168.174.120:80 -r 192.168.174.167 -g
    保存定义好的规则文件
        ipvsadm -S > /etc/sysconfig/ipvsadm

6.查看定义好的规则
ipvsadm -ln

7.在web服务器上安装启动nginx
yum install nginx -y
systemctl start nginx

8.创建index.html
echo "rs-1" /usr/share/nginx/html/index.html

9.在rs中绑定lo网卡
ip addr add dev lo 192.168.174.120/32

10.临时设置使rs对arp保持静默
echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore

11.开启路由转发、匹配精确ip地址回包(保证rs将数据包返还给客户端)
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce

12.测试http://192.168.174.120