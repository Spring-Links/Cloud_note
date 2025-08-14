**查看firewall状态**
```
-- 该提示代表服务器中没有防火墙应用
Unit firewalld.service could not be found.
```

**安装防火墙**
`yum install firewalld firewalld-config`

**启动防火墙**
`systemctl start firewalld`

**添加端口号**
`firewall-cmd --zone=public --permanent --add-port=8080/tcp`

**加载规则**
`firewall-cmd --reload`

**查看开放的端口号**
```
firewall-cmd --list-all
-- 观察ports的值
ports：8080/tcp（代表端口已经开放）
```

==如果是云服务器还要再安全组策略中开放相应的端口==