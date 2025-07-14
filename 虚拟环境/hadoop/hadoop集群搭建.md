#### 将hadoop文件上传至 /export/softwares

#### 将文件解压至 /export/servers
> tar -zxvf hadoop-2.7.5.tar.gz -C ../servers/

#### hadoop文件配置
```
目录：/export/servers/hadoop-2.7.5/etc/hadoop
详见至conf文件
注意：将三台主机名分别添加至/export/servers/hadoop-2.7.5/etc/hadoop/slaves,每个主机名占用一行
```

#### 使用scp将文件进行远程分发
```
scp 本地文件路径 root@IP地址:远程路径
```

#### 编辑、重载、验证环境变量
> vim /etc/profile
> export HODOOP_HOME=/export/servers/hadoop-2.7.5
> export PATH=\$HODOOP_HOME/bin:$PATH
> source /etc/profile
> hdfs

#### 初始化hdfs
> /export/servers/hadoop-2.7.5/bin/hdfs namenode -format

#### 启动集群
> /export/servers/hadoop-2.7.5/sbin/start-dfs.sh
> /export/servers/hadoop-2.7.5/sbin/start-yarn.sh
> /export/servers/hadoop-2.7.5/sbin/mr-jobhistory-daemon.sh start historyserver

#### 通过web查看启动状态
```
http://node01:50070
http://node01:8088
http://node01:19888
```
