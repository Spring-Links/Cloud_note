#### 正确配置java环境
```
vim /etc/profile
source /etc/profile
export JAVA_HOME=/usr/local/java/jdk1.8.0_202
export PATH=$JAVA_HOME/bin:$PATH
```
#### 将hadoop文件上传至 /export/softwares
> tar -zxvf zookeeper-3.4.9.tar.gz -C ../servers

#### 复制zookeeper的conf文件
> cp /export/servers/zookeeper-3.4.9/conf/zoo_sample.cfg zoo.cfg

#### 在zookeeper根目录下创建文件夹zkdatas
> mkdir -p /export/servers/zookeeper-3.4.9/zkdatas

#### 编辑zoo.cfg文件
> vim /export/servers/zookeeper-3.4.9/conf/zoo.cfg

#### 配置文件内容
```
#数据保存路径
dataDir=/export/servers/zookeeper-3.4.9/zkdatas
# 保留多少个快照
autopurge.snapRetainCount=3
# 日志多少小时清理一次
autopurge.purgeInterval=1
# 集群中服务器地址
server.1=node01:2888:3888
server.2=node02:2888:3888
server.3=node03:2888:3888
```
#### 在zkdatas目录下创建文件myid，并echo值
> touch /export/servers/zookeeper-3.4.9/zkdatas/myid
> echo 1 > myid 

#### 使用scp命令远程分发文件,并向其myid中添加值
> scp -r /export/servers/zookeeper-3.4.9/ node02:/export/servers/
> scp -r /export/servers/zookeeper-3.4.9/ node03:/export/servers/

#### 修改其余两台机器的值
> echo 2 > /export/servers/zookeeper-3.4.9/zkdatas/myid
> echo 3 > /export/servers/zookeeper-3.4.9/zkdatas/myid

#### 启动并查看zookeeper运行状态
> /export/servers/zookeeper-3.4.9/bin/zkServer.sh start
> /export/servers/zookeeper-3.4.9/bin/zkServer.sh status