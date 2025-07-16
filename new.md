以下是一个详细的LVS + Keepalived + Nginx + Tomcat + MySQL高可用集群部署指南，按照机器IP分组操作：

---

### **环境规划**
| 角色                | IP地址            |
|---------------------|-------------------|
| LVS Master         | 192.168.174.124  |
| LVS Backup         | 192.168.174.125  |
| Nginx 节点1        | 192.168.174.166  |
| Nginx 节点2        | 192.168.174.167  |
| Tomcat 节点1       | 192.168.174.177  |
| Tomcat 节点2       | 192.168.174.178  |
| MySQL Master       | 192.168.174.188  |
| MySQL Slave        | 192.168.174.189  |
| VIP (虚拟IP)       | 192.168.174.200  |

---

### **一、LVS + Keepalived 配置 (124/125)**
#### **1. 安装依赖**
```bash
# 在124和125执行
yum install -y keepalived ipvsadm
```

#### **2. 配置Keepalived (主节点124)**
`/etc/keepalived/keepalived.conf`：
```conf
vrrp_instance VI_1 {
    state MASTER
    interface eth0               # 修改为实际网卡名
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.174.200/24
    }
}

virtual_server 192.168.174.200 80 {
    delay_loop 6
    lb_algo wrr
    lb_kind DR
    persistence_timeout 50
    protocol TCP

    real_server 192.168.174.166 80 {
        weight 1
        TCP_CHECK {
            connect_timeout 3
            connect_port 80
        }
    }
    real_server 192.168.174.167 80 {
        weight 1
        TCP_CHECK {
            connect_timeout 3
            connect_port 80
        }
    }
}
```

#### **3. 配置Keepalived (备节点125)**
- 修改`state`为`BACKUP`
- 修改`priority`为`90`
- 其他配置与主节点相同

#### **4. 启动服务**
```bash
systemctl start keepalived && systemctl enable keepalived
```

---

### **二、Nginx配置 (166/167)**
#### **1. 安装Nginx**
```bash
yum install -y nginx
```

#### **2. 配置负载均衡**
`/etc/nginx/conf.d/loadbalance.conf`：
```conf
upstream tomcat_cluster {
    server 192.168.174.177:8080 weight=2;  # 权重2
    server 192.168.174.178:8080 weight=1;  # 权重1
    keepalive 32;
}

server {
    listen 80;
    location / {
        proxy_pass http://tomcat_cluster;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### **3. 启动服务**
```bash
systemctl start nginx && systemctl enable nginx
```

---

### **三、Tomcat配置 (177/178)**
#### **1. 安装JDK**
```bash
yum install -y java-1.8.0-openjdk-devel
```

#### **2. 安装Tomcat**
```bash
wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.68/bin/apache-tomcat-9.0.68.tar.gz
tar -xzf apache-tomcat-9.0.68.tar.gz -C /opt
mv /opt/apache-tomcat-9.0.68 /opt/tomcat
```

#### **3. 配置Tomcat**
`/opt/tomcat/conf/server.xml`：
```xml
<Connector port="8080" protocol="HTTP/1.1" 
           connectionTimeout="20000"
           redirectPort="8443" 
           URIEncoding="UTF-8"/>
```

#### **4. 部署测试应用**
```bash
echo "<h1>Tomcat Node 177</h1>" > /opt/tomcat/webapps/ROOT/index.html  # 177节点
echo "<h1>Tomcat Node 178</h1>" > /opt/tomcat/webapps/ROOT/index.html  # 178节点
```

#### **5. 配置LVS DR脚本**
创建`/etc/init.d/realserver`：
```bash
#!/bin/bash
VIP=192.168.174.200

case "$1" in
start)
    echo "Starting LVS RealServer"
    /sbin/ifconfig lo:0 $VIP netmask 255.255.255.255 broadcast $VIP up
    echo 1 > /proc/sys/net/ipv4/conf/lo/arp_ignore
    echo 2 > /proc/sys/net/ipv4/conf/lo/arp_announce
    echo 1 > /proc/sys/net/ipv4/conf/all/arp_ignore
    echo 2 > /proc/sys/net/ipv4/conf/all/arp_announce
    ;;
stop)
    echo "Stopping LVS RealServer"
    /sbin/ifconfig lo:0 down
    echo 0 > /proc/sys/net/ipv4/conf/lo/arp_ignore
    echo 0 > /proc/sys/net/ipv4/conf/lo/arp_announce
    echo 0 > /proc/sys/net/ipv4/conf/all/arp_ignore
    echo 0 > /proc/sys/net/ipv4/conf/all/arp_announce
    ;;
*)
    echo "Usage: $0 {start|stop}"
    exit 1
esac
```
**启用脚本**：
```bash
chmod +x /etc/init.d/realserver
/etc/init.d/realserver start  # 两台Tomcat都执行
```

#### **6. 启动Tomcat**
```bash
/opt/tomcat/bin/startup.sh
```

---

### **四、MySQL主从配置 (188/189)**
#### **1. 安装MySQL (两台)**
```bash
yum install -y mysql-server
systemctl start mysqld
```

#### **2. 主库配置 (188)**
`/etc/my.cnf`：
```ini
[mysqld]
server-id=1
log-bin=mysql-bin
binlog-do-db=webapp
```
**创建复制用户**：
```sql
CREATE USER 'repl'@'192.168.174.%' IDENTIFIED BY 'Repl@123';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'192.168.174.%';
FLUSH PRIVILEGES;
```

#### **3. 从库配置 (189)**
`/etc/my.cnf`：
```ini
[mysqld]
server-id=2
relay-log=mysql-relay-bin
```

#### **4. 启动主从复制**
1. 在主库查状态：
   ```sql
   SHOW MASTER STATUS;  # 记录File和Position
   ```
2. 在从库配置同步：
   ```sql
   CHANGE MASTER TO
     MASTER_HOST='192.168.174.188',
     MASTER_USER='repl',
     MASTER_PASSWORD='Repl@123',
     MASTER_LOG_FILE='mysql-bin.000001',
     MASTER_LOG_POS=154;
   START SLAVE;
   ```
3. 验证同步状态：
   ```sql
   SHOW SLAVE STATUS\G;  # 确保Slave_IO_Running和Slave_SQL_Running为Yes
   ```

---

### **五、集群验证**
#### **1. 测试LVS高可用**
```bash
curl http://192.168.174.200  # 应轮询返回Tomcat页面
# 关闭主LVS (124)，VIP自动漂移到125
```

#### **2. 测试Nginx负载均衡**
```bash
# 在166/167分别执行
tail -f /var/log/nginx/access.log  # 观察请求分发比例
```

#### **3. 测试MySQL主从**
- 主库创建数据：
  ```sql
  CREATE DATABASE webapp;
  USE webapp;
  CREATE TABLE test(id INT);
  INSERT INTO test VALUES(1);
  ```
- 从库验证：
  ```sql
  SELECT * FROM webapp.test;  # 应同步数据
  ```

#### **4. 测试故障转移**
- 关闭任意Tomcat节点：请求自动转移到其他节点
- 关闭MySQL主库：应用应切换到从库（需应用支持）

---

> **关键说明**：
> 1. 所有节点需关闭防火墙：`systemctl stop firewalld`
> 2. 确保VIP绑定在LVS主节点：`ip addr show eth0`
> 3. ARP抑制验证：`sysctl -a | grep arp_ignore`
> 4. 生产环境建议添加：健康检查脚本、日志监控、SSL加密

此架构实现了：
- ✅ LVS四层负载 + Keepalived高可用（毫秒级切换）
- ✅ Nginx七层负载 + 权重调度
- ✅ Tomcat集群 + 故障自动转移
- ✅ MySQL主从复制 + 数据冗余
- ✅ 全链路无单点故障