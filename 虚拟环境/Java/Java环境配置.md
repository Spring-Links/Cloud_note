#### 创建 /export/softwares、/export/servers文件夹
> mkdir -p /export/softwares
> mkdir -p /export/servers

#### 使用xftp将Java文件上传至 /export/softwares

#### 将上传的文件解压至 /export/servers中
> tar -zxvf jdk-8u202-linux-x64.tar.gz -C ../servers

#### 编辑、重载环境变量
> vim /etc/profile
> export JAVA_HOME=/export/servers/jdk1.8.0_202
> export PATH=\$JAVA_HOME/bin:$PATH
> source /etc/profile

#### 验证java环境
> java -version