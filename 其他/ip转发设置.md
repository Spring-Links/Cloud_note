**非持久化设置：**`/proc/sys/net/ipv4/ip_forward`
- 0：关闭
- 1：开启

**持久化设置：**
```
vim /etc/sysctl.conf
-- 添加
net.ipv4.ip_forward=1
```

**设置生效：** `sysctl -p`

**如果sysctl未运行可以使用systemctl查看**
`systemctl status sysctl`