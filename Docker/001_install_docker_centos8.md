**解决冲突**
- ==podman包冲突==
```
-- 报错如下：
package podman-3:4.9.4-0.1.module_el8+971+3d3df00d.x86_64 from @System requires runc >= 1.0.0-57, but none of the providers can be installed

-- 报错原因：
系统中存在podman

-- 解决办法：
yum erase -y podman buildah
```


- ==缺少containerd.io==
```
-- 报错如下：
package docker-ce-3:20.10.9-3.el8.x86_64 from docker-ce-stable requires containerd.io >= 1.4.1, but none of the providers can be installed

-- 报错原因：
centos8默认使用podman代替docker，所以需要安装containerd.io

-- 解决办法：
yum install -y https://download.docker.com/linux/centos/8/x86_64/stable/Packages/containerd.io-1.5.11-3.1.el8.x86_64.rpm
```

**安装docker**
- **卸载系统中存在的docker**
- **安装软件包**
`sudo yum install -y yum-utils device-mapper-persistent-data lvm2`

- **设置阿里源镜像**
`sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo`

- **查看docker可用版本**
`yum list docker-ce --showduplicates | sort -r`

- **安装指定版本**
`sudo yum install -y docker-ce-20.10.9-3.el8 docker-ce-cli-20.10.8`

- **启动docker**
`systemctl start docker & systemctl enable docker`