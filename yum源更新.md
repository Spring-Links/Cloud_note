备份旧的repo文件
`mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup`

下载第三方repo文件
`wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo `

清除缓存文件
`yum clean all`

下载缓存文件
`yum makecache`

更新yum
`yum -y update`
