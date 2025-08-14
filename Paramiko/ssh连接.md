ssh server建立server public key，对应文件/etc/ssh/ssh_host_*文件
ssh client发出连接请求
ssh server发送server public key给ssh client 
ssh client 比较server public key，同时计算自己的client public/private key
ssh client 发送client public key到ssh server
开始连接，双向加密