**ansible配置文件检查顺序**
- 先检查ANSIBLE_CONFIG变量定义的配置文件
- 当前目录下的./ansible.cfg
- 家目录下~/ansible.cfg
- /etc/ansible/ansible.cfg

**ansible工作流程**
- **陈述：** master连接被管理的主机，将模块（脚本）文件传入被管理的主机并执行 

**设置主机名及解析**
- **在所有服务器上配置主机名**
`hostnamectl set-hostname node01`
- **将各主机名及ip解析写入控制端主机中**
`vim /etc/hosts`

**生成及分发密钥**
- **生成密钥**
`ssh-keygen -f /root/.ssh/id_rsa -N " `
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

**安装python3.12**
```
验证环境
python3.12 --version
```

**安装ansible**
```
-- 使用pip3.12安装
pip3.12 install ansible
# pip3.12 install --user ansible --用户级安装

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

**命令行基本格式**
`ansible 主机集合 -m 模块名 -a 参数`
- -k：使用密码进行远程而不使用的密钥
- -i：指定特定的主机列表文件

**查看所有主机列表**
`ansible all --list-hosts`
- all是ansible默认带的组

**ping模块**
`ansible node01,node02 -m ping`

**在被控主机上使用linux命令**
==无论是command还是shell都不能执行交互式命令，如vim等==
- command
    - `ansible node01 -m command -a '要执行的命令'`
- shell
  - `ansible node01 -m shell -a '要执行的命令'`
**模块**
```
-- 列出所有模块
ansible-doc -l 
```
```
-- 过滤模块
ansible-doc -l | grep yum
```
```
-- 查看模块帮助
ansible-doc yum 
```

**shell模块**
- **在指定路径下执行多个操作**
  - `ansible node -m shell -a 'chdir=/etc/ansible touch a.txt b.txt c.txt'`

- **create**
  - create 文件名 -文件存在，不执行shell-
- **removes**
  - removes 文件名 -文件不存在，不执行shell-

**script**
`ansible node01 -m script -a '脚本文件'`
- script：将脚本文件出入被控主机并执行，当执行完成时就将文件删除
- 如果脚本不是shell脚本，没有执行权限也可以执行脚本

**file**
- **新建文件**
`ansible node01 -m file -a 'path=/tmp/file.txt state=touch'`

- **创建目录**
`ansible node01 -m file -a 'path=/tmp/newdir state=directory'`

- **修改文件或目录权限**
`ansible node01 -m file -a 'path=/tmp/file.txt owner=sshd group=adm mode=777'`

- **删除目录**
`ansible node01 -m file -a 'path=tmp/mydir state=absent'`

- **删除文件**
`ansible node01 -m file -a 'path=/tmp/file.txt state=absent'`

- **创建软链接**
`ansible node01 -m file -a 'src=/etc/hosts path=/tmp/host.txt state=link'`

**copy**
- **拷贝现有文件**
`ansible node01 -m copy -a 'src=~/aaa.txt dest=/tmp'` -不改动文件名传入被控主机-
`ansible node01 -m copy -a 'src=~/aaa.txt dest=/tmp/bbb.txt'` -修改文件名并传入被控主机-

- **拷贝现写文件**
`ansible node01 -m copy -a 'content='hello world\n shanghai' dest=/tmp/new.txt'` -\n：换行-

**fetch**
==将被控主机文件拷贝至本地主机==
`ansible node01 -m fetch -a 'src=/etc/hosts dest=~/'`

**lineinfile/replace**
- **向文件中添加内容，默认在最后一行**
`ansible node01 -m lineinfile -a 'path=/etc/hosts line='hello world''`

- **在特定内容(如：Kernel)后添加**
`ansible node -m lineinfile -a 'path=/etc/hosts line='insert' insertafter='Kernel''`

- **替换内容**
`ansible node01 -a lineinfile -a 'path=/etc/tmp regexp='hello' line='ni hao''`
  - **陈述：** 在该文件中使用正则表达式匹配到hello并将hello替换为ni hao，如果没有匹配到就在文件最后一行写入ni hao，如果匹配到多行则进替换最后一行 

- **replace**
`ansible node01 -m replace -a 'path=/etc/tmp regexp=hello replace=ni hao' `
  - **陈述：** 将该文件全文进行替换

**user**
- **创建用户**
`ansible node01 -m user -a 'name=tuser1'`

- **创建账户并设置对应账户的属性**
`ansible node01 -m user -a 'name=newuser uid=1010 group=adm groups=daemon,root home=/home/newuser' `

- **给现有用户设置密码**
`ansible node01 -m user -a 'name=newuser password={{'your_password'|password_hash('sha512')}}'`

- **给现有用户设置附加组**
`ansible node01 -m user -a 'name=username groups=root,daemon' `

- **删除账户**
`ansible node01 -m user -a 'name=username state=absent' `

- **删除账户同时删除家目录和邮箱**
`ansible node01 -m user -a 'name=username state=absent remove=true' `

**yum_repository**
- **添加yum源**
`ansible node01 -m yum_repository -a 'name=myyum description=hello baseurl=ftp://192.168.174.160/centos gpgcheck=no' `
  - **陈述：** 新建yum源配置文件/etc/yum.repos.d/myyum.repo，yum源文件名为myyum，内容为：
  ```
  [myyum]
  baseurl = ftp://192.168.174.160/centos
  gpgcheck = 0
  name = hello 
  ```

- **删除yum源**
`ansible node01 -m yum_repository -a 'name=myyum state=absent' `

**yum**
- **安装**
`ansible node01 -m yum -a 'name=app_name state=present' `

- **卸载**
`ansible node01 -m yum -a 'name=app_name state=absent' `

- **升级**
`ansible node01 -m yum -a 'name=app_name state=latest' `

**service**
- **启动服务**
`ansible node01 -m service -a 'name=app_name state=started' `

- **停止服务**
`ansible node01 -m service -a 'name=app_name state=stopped' `

- **重启服务**
`ansible node01 -m service -a 'name=app_name state=restarted' `

- **开机自启**
`ansible node01 -m service -a 'name=app_name enabled=yes' `

**逻辑卷LVM**

**sudo提权**
- **修改sudoers方法**
  - visudo
  - vim /etc/sudoers

- **授权格式**
  - 用户或组 主机列表=(提权身份) [NOPASSWD]:命令列表
  如：monika     ALL=(root)      /usr/bin/systemctl

- **普通用户查看sudo授权情况**
  - sudo -l

**配置sudo提权**
- **为被管理主机创建系统账户**
用户名：alice 密码：user
`ansible all -m user -a "name=alice password={{'user'|password_hash('sha512')}}" `

- **配置sudo让alice可以管理系统服务**
`ansible all -m lineinfile -a "path=/etc/sudoers line='alice ALL=(ALL) /usr/bin/systemctl' "`

**ansible配置文件进阶**
[defaults]
inventory=~/ansible/hosts
remote_user=alice #以什么用户远程被管理主机
[privilege_escalation]
become=ture #是否切换用户
become_method=sudo #如何为什么用户
become_user=root #切换为什么用户
become_ask_pass=no #sudo是否需要密码

**主机清单**
```
-- 使用场景：个别账户名不同、有些主机没有密钥、有些主机ssh端口不是22
[testhost]
node01 ansible_ssh_port=220 ansible_ssh_private_key_file=密钥文件 #自定义端口、连接的密钥文件
node02 ansible_ssh_user=jack #自定义用户名
node03 ansible_ssh_pass=密码 #自定义密码而不使用密钥
```

**ansible playbook（剧本）**
- **yaml格式**
  - "#" 代表注释，一般第一行为三个横杠
  - 键值对使用":"表示，数组使用"-"表示
  - 缩进必须由两个或以上的空格组成
  - 相同层级的缩进必须对齐
  - 全文不能使用tab键
  - 区分大小写，扩展名为yml或yaml
  - 跨行数据使用>或| （|会保留换行符）
  - playbook由一个或多个play组成
  - 每个play中可以包含
    - hosts(主机)、tasks(任务)
    - variables(变量)、roles(角色)、handlers
  - 使用ansible-playbook命令运行playbook剧本

- **键值对数据**
```
"诗仙": "李白"
```
```
"诗仙":
  "李白"
```
  - 键值之间使用":"分割
  - ":"后面必须有空格
  - 缩进代表层级关系

- **数组数据**
```
-- 纯数组
- "李白"
- "杜甫"
- "白居易"
- "唐僧"
```
```
-- 键值对和数组进行组合
"诗人":
  - "李白"
  - "杜甫"
  - "白居易"
```
  - **示例：**
  ```
  --- #喜欢的电影
  -  芳华
  -  战狼
  -  霸王别姬
  ```
  ```
  --- #人物描述
  -  姓名：李白
     年龄：61
     作品：蜀道难
     好友：汪伦
  ```

**playbook**
- **新建用户**
- **新建磁盘分区**
- **软件安装及升级**

