主机划分：
  192.168.174.124
  setenforce 0
  systemctl stop firewalld
  192.168.174.125
  192.168.174.133
  192.168.174.134


1. 关闭服务器的防火墙和selinux
2. 在124、125中安装ipvsadm、keepalived
3. 在133、134中安装nginx
4. 划分192.168.174.200为vip
5. 在124中进行操作
6. 开启ip转发在lvs服务器中`echo 1 > /proc/sys/net/ipv4/ip_forward`
7. 将vip绑定到ens160上，并创建一个虚拟子接口ens160:0 `ip addr add 192.168.174.200/32 dev ens160 label ens160:0`
8. 开启这个虚拟接口
9. 添加路由规则将目标为200的流量都通过创建的虚拟子接口
10. 创建一个虚拟访问并设置轮询方法
11. 将vip与rip进行绑定并选择dr模式
12. 查看ipvs的规则
13. 在133和134中操作
14. 将vip绑定到lo口上，并创建虚拟子接口
15. 开启这个接口
16. 添加路由规则将目标为vip的流量都通过lo:0接口出去
17. 设置arp响应和忽略规则，开启nginx服务
18. 此时在物理机访问vip测试集群是否连通
19. 在124、125中配置keepalived文件
20. 在主节点中配置lvs的唯一id
21. 指定keepalived的角色为master
22. 设置网卡
23. 设置虚拟路由编号，主备节点一致
24. 设置竞选优先级master大于backup
25. 检测主备密码
26. 设置vip地址
27. 定义vip的服务包括调度算法
28. lvs的工作模式
29. 将rip写入文件并设置权重
30. 重启keepalived服务
31. 在125中设置lvs唯一id
32. 指定角色为backup
33. 调整竞选优先级
34. 其他保持一致
35. 重启keepalived服务
36. 在物理机中访问vip
37. 将master的keepalived服务关闭
38. 重新测试vip是否能正常访问
39. 在backup节点中通过`ip addr show ens160`,`ipvsadm -Ln`查看lvs规则是否发生转移