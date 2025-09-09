**ansible工作流程**
- **陈述：** master连接被管理的主机，将模块（脚本）文件传入被管理的主机并执行 

**设置主机名及解析**
- **在所有服务器上配置主机名**
`hostnamectl set-hostname node01`
- **将各主机名及ip解析写入控制端主机中**
`vim /etc/hosts`

**生成及分发密钥**
- **生成密钥**
`ssh-keygen -f /root/.ssh/id_rsa -N '' `
- **传输密钥**
```
for i in node01 node02 node03 
do
  ssh-copy-id $i
done
```
- **测试ssh密钥是否配置成功**
```
-- 在master主机中测试是否能无密码连接
ssh node01
exit
ssh node02
exit
```

**更新EPEL源**
```
sudo yum install -y epel-release
```

**安装python3和pip**
```
sudo dnf install -y python3 python3-pip   # 安装python3和pip3
python3 --version
pip3 install --upgrade pip   # 更新pip
```

**安装ansible（阿里源）**
```pip3 install ansible -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
-- 验证安装
ansible --version
```

**编写ansible配置文件、主机文件**
```
mkdir /etc/ansible
vim /etc/ansible/ansible.cfg
vim /etc/ansible/hosts
-- 测试是否连通
```

**ansible配置文件检查顺序**
- 先检查ANSIBLE_CONFIG变量定义的配置文件
- 当前目录下的./ansible.cfg
- 家目录下~/ansible.cfg
- /etc/ansible/ansible.cfg