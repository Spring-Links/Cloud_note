==推荐版本==
```
docker-ce-20.10.8-3.el8
docker-ce-cli-20.10.8
kubectl-1.19.8
kubelet-1.19.8
kubeadm-1.19.8
```

**查看系统版本**
`cat /etc/redhat-release`

**设置主机名**
`vim /etc/hostname`

**解析主机名**
`vim /etc/hosts`

**同步时间**
`systemctl start chronyd`

**关闭防火墙**
`systemctl stop firewalld`

**禁用iptables**
`systemctl stop iptables`

**禁用selinux**
```
setenforce 0
vim /etc/selinux/config
Permissive
```

**禁用swap分区（注释swap所在行）**
`vim /etc/fstab`

**修改linux内核参数**
```
vim /etc/sysctl.d/kubernetes.conf

net.brige.brige-nf-call-ip6tables = 1
net.brige.brige-nf-call-iptables = 1
net.ipv4.ip_forward = 1

sysctl -p
```

**加载网桥过滤模块**
`modprobe br_netfilter`

**查看模块是否加载成功**
`lsmod | grep br_netfilter`

**安装配置ipvsadm ipset**
`yum install -y ipvsadm ipset`

**添加需要加载的模块**
```
vim /etc/sysconfig/modules/ipvs.modules

#!/bin/bash
modprobe -- ip_vs
modprobe -- ip_vs_rr
modprobe -- ip_vs_wrr
modprobe -- ip_vs_sh
modprobe -- nf_conntrack
```

**为文件添加执行权限**
`chmod +x /etc/sysconfig/modules/ipvs.modules `

**执行脚本文件**
`/bin/bash /etc/sysconfig/modules/ipvs.modules`

**查看模块是否加载成功**
`lsmod | grep -e ip_vs -e nf_conntrack_ipv4`

**重启服务器，并检查设置是否生效**
```
reboot
getenforce
free -m
```

****

**安装特定版本docker**
==详见Note\Docker\centos8_install_docker.md==

- **配置镜像站地址**
`vim /etc/docker/daemon.json`
``` 
{
        "registry-mirrors": [
                "https://docker.m.daocloud.io",
                "https://docker.1panel.live",
                "https://hub.rat.dev"

        ]

}
```

```
-- 加载daemon-reload
systemctl daemon-reload

-- 重启docker
systemctl restart docker

-- 检查docker版本
docker version
```

****

**安装kubernetes组件**
- **添加kubernetes镜像源**
```
-- 添加镜像源（新版本）
vim /etc/yum.repos.d/kubernetes.repo

[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes-new/core/stable/v1.28/rpm/
enabled=1
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes-new/core/stable/v1.28/rpm/repodata/repomd.xml.key



-- 添加镜像源（旧版本）
vim /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg

-- 卸载epel源
rpm -qa | grep epel
yum -y remove epel-release.noarch 

-- 安装最新的epel源
yum install -y https://mirrors.aliyun.com/epel/epel-release-latest-8.noarch.rpm

-- 替换源
sed -i 's|^#baseurl=https://download.example/pub|baseurl=https://mirrors.aliyun.com|' /etc/yum.repos.d/epel*
sed -i 's|^metalink|#metalink|' /etc/yum.repos.d/epel*
```

- **安装kubelet kubeadm kubectl**
```
-- 安装组件
yum install -y kubelet kubeadm kubectl

-- 查看版本
kubeadm version

-- 设置开机自启
systemctl enable kubelet
```

-- **设置k8s命令自动补全**
```
# yum -y install bash-completion
# source /usr/share/bash-completion/bash_completion
# source <(kubectl completion bash)
# echo "source <(kubectl completion bash)" >> ~/.bashrc
```

- **配置kubelet的cgroup**
```
vim /etc/sysconfig/kubelet

KUBELET_CGROUP_ARGS="--cgroup-driver=systemd"
KUBE_PROXY_MODE="ipvs"
```

- **准备集群镜像**
  - **查看需要准备的镜像**
`kubeamd config images list`

  - **下载镜像**
```
images=(
    kube-apiserver:v1.19.8
    kube-controller-manager:v1.19.8
    kube-scheduler:v1.19.8
    kube-proxy:v1.19.8
    pause:3.2
    etcd:3.4.13-0
    coredns:1.7.0
)

for imageName in ${images[@]} ; do
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
    docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
    docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
done
```

  - **检查镜像下载的情况**
`docker images`

- **集群初始化**
==仅在master节点中执行==
==本次安装的k8s版本为1.28.15==
==确保containerd.io版本为1.6.32-3.1==
- **进行初始化拉取镜像**
```
kubeadm init --image-repository=registry.aliyuncs.com/google_containers \
    --kubernetes-version=v1.19.8 \
    --pod-network-cidr=10.244.0.0/16 \
    --service-cidr=10.96.0.0/12 \
    --apiserver-advertise-address=192.168.174.144
```

****

**解决冲突**
- ==缺少tc流量控制工具==
```
-- 报错如下：
[WARNING FileExisting-tc]: tc not found in system path

-- 报错原因：
系统中未安装tc工具

-- 解决办法：
yum install -y iproute-tc
```

****
官方初始化
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

将node节点加入集群

查看集群状态
kubectl get nodes
****

**安装网络插件**
- **下载flannel网络插件**
`https://github.com/flannel-io/flannel/releases`

- **修改文件中的源地址为阿里源**
- **应用网络插件**
` kubectl apply -f kube-flannel.yml`
- **查看集群中网络是否能够通讯**
==STATUS的值由NotReady变为Ready==
`kubectl get nodes`

**测试集群环境是否正常**
```
-- 部署nginx
kubectl create deployment nginx --image=nginx:1.14-alpine

开放端口
kubectl expose deployment nginx --port=80 --type=NodePort

-- 查看pod中的nginx
kubectl get pod

-- 查看服务中的nginx
kubectl get svc

-- 在外部浏览器中访问nginx服务
```

