阶段2：LVS+Keepalived层（124/125）配置详细步骤

步骤2.1：在124和125安装软件
在 192.168.174.124 和 192.168.174.125 上执行：
sudo yum install ipvsadm keepalived -y

步骤2.2：配置Keepalived主节点(124)
sudo vi /etc/keepalived/keepalived.conf

步骤2.3：配置Keepalived备节点(125)
sudo vi /etc/keepalived/keepalived.conf

步骤2.4：启动服务（两台都启动）
sudo systemctl start keepalived
sudo systemctl enable keepalived

步骤2.5：验证VIP和状态（主节点124）
ip addr show ens33 | grep 192.168.174.200  # 应该看到VIP绑定
sudo ipvsadm -Ln  # 查看LVS规则

步骤2.6：模拟故障切换测试
在 192.168.174.124 上停止keepalived：
sudo systemctl stop keepalived
在 192.168.174.125 上检查VIP：
ip addr show ens33 | grep 192.168.174.200  # 应该看到VIP已漂移
在 192.168.174.125 上检查LVS规则：
sudo ipvsadm -Ln
在 192.168.174.124 上恢复服务：
sudo systemctl start keepalived

阶段3：Nginx层（166/167）配置详细步骤

步骤3.1：在166和167安装Nginx
sudo yum install epel-release -y
sudo yum install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

步骤3.2：配置DR模式脚本(/etc/init.d/realserver)（166和167都要执行）
赋予权限并执行realserver文件

验证脚本执行效果：
在 192.168.174.166 和 192.168.174.167 上执行：
ip addr show lo:0  # 应看到192.168.174.200
route -n | grep 192.168.174.200  # 应看到路由指向lo

步骤3.3：验证LVS状态和Nginx接入
在 192.168.174.124 上检查：
sudo ipvsadm -Ln
输出应包含两条真实服务器记录

在任意机器上测试VIP访问：
curl http://192.168.174.200  # 应看到Nginx欢迎页

在 192.168.174.166 上停止Nginx：
sudo systemctl stop nginx

在 192.168.174.124 上查看LVS状态：
sudo ipvsadm -Ln
166的状态应变为INACTIVE

再次curl访问VIP，应仍能访问

阶段4：Tomcat层（177/178）配置详细步骤

步骤4.1：在177和178安装Tomcat
sudo yum install java-11-openjdk -y
wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz
sudo tar -zxvf apache-tomcat-*.tar.gz -C /opt/
sudo mv /opt/apache-tomcat-9.0.85 /opt/tomcat

177上修改默认端口（避免冲突）：
在 192.168.174.177 上执行：
sudo sed -i 's/port="8080"/port="8081"/' /opt/tomcat/conf/server.xml

创建测试页面（区分两台）：
在 192.168.174.177 上：
echo "Tomcat Server 177" | sudo tee /opt/tomcat/webapps/ROOT/index.html
在 192.168.174.178 上：
echo "Tomcat Server 178" | sudo tee /opt/tomcat/webapps/ROOT/index.html

启动Tomcat：
在 192.168.174.177 和 192.168.174.178 上执行：
sudo /opt/tomcat/bin/startup.sh

步骤4.2：配置Nginx反向代理（166和167）
upstream tomcat_cluster {
    server 192.168.174.177:8081;  # 177节点
    server 192.168.174.178:8080;  # 178节点
}

server {
    listen 80;
    server_name localhost;
    
    location / {
        proxy_pass http://tomcat_cluster;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
重启Nginx

步骤4.3：验证Tomcat接入
在 192.168.174.166 上测试Nginx代理：
curl http://localhost  # 应随机返回177或178的内容

在任意机器上测试VIP访问：
curl http://192.168.174.200  # 应返回Tomcat内容

在 192.168.174.177 上停止Tomcat：
sudo /opt/tomcat/bin/shutdown.sh

再次访问VIP，应只返回178的内容



分阶段测试计划

阶段测试1：LVS基础功能
在 192.168.174.124 上：
ip addr show ens33 | grep 200  # 应看到VIP

在 192.168.174.125 上：
sudo systemctl stop keepalived  # 停止备节点
主节点状态应不变

在 192.168.174.124 上：
sudo systemctl stop keepalived
在 192.168.174.125 上：
ip addr show ens33 | grep 200  # 应看到VIP漂移

阶段测试2：Nginx接入
在 192.168.174.166 上：
curl -I http://localhost  # 应返回200 OK

在 192.168.174.124 上：
sudo ipvsadm -Ln  # 应看到两个Nginx后端

在 192.168.174.166 上：
sudo systemctl stop nginx
在 192.168.174.124 上：
sudo ipvsadm -Ln  # 166应显示为INACTIVE

阶段测试3：Tomcat接入
在 192.168.174.177 上：
curl http://localhost:8081  # 应返回"Tomcat Server 177"

在 192.168.174.166 上：
curl http://localhost  # 应随机返回177或178内容

在 192.168.174.200 上：
curl http://localhost  # 通过VIP访问应成功

最终集成测试
完整链路测试：
curl http://192.168.174.200

高可用连环测试：
停止主LVS(124)
ssh 192.168.174.124 sudo systemctl stop keepalived
curl http://192.168.174.200  # 应仍可访问（125接管）

停止一台Nginx(166)
ssh 192.168.174.166 sudo systemctl stop nginx
curl http://192.168.174.200  # 应仍可访问（LVS转发到167）

停止一台Tomcat(177)
ssh 192.168.174.177 /opt/tomcat/bin/shutdown.sh
curl http://192.168.174.200  # 应只返回178的内容