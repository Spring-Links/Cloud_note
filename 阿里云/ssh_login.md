**Public Key登录服务器**
1. 在所在实例中创建密钥对
2. 将创建的密钥对与实例进行绑定
3. 重启服务器使密钥对生效
4. 打开xshell，以Public Key方式登录

**密码登陆服务器**
1. 使用Public Key登录
2. vim /etc/ssh/sshd_config
3. 将PasswordAuthentication no改为yes
4. 重启sshd服务 systemctl restart sshd
5. 在xshell中使用密码登录