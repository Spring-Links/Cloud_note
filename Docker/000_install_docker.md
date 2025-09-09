**docker安装地址**
~~`https://get.docker.com/`~~

**centos安装docker**
- **安装必要的软件包**
`dnf install -y yum-utils device-mapper-persistent-data lvm2`
- **添加docker官方仓库**
  - **官方源：** `dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo `
  - **阿里源：** `dnf config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo`
- **安装docker**
`dnf install -y docker-ce docker-ce-cli containerd.io`
- **开启docker服务**
`systemctl start docker`
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

- **docker pull命令格式**
  - `docker pull docker.io/library/nginx:latest`
    - `docker.io：`仓库地址/注册表
    - `library:`命名空间（作者名）
    - `nginx：`标签名（版本号）

**查看已经拉取的镜**
`docker images`

**删除拉取的镜像**
`docker rmi images_id/images_name`

==运行以后的镜像就被称为容器==

**运行容器**
`docker run images_name`

**查看运行的容器**
`docker ps`

**后台运行容器**
`docker run -d images_name`

**映射端口运行**
`docker run -p 80:80 nginx`
- `80:80` 宿主机端口:容器端口

**删除容器**
`docker rm -f container_id`

**挂载卷**
- **绑定挂载**
  - **格式：**`docker run -v `
  - **示例：**`docker run  -p 80:80 -v /home/nginx.index:/usr/share/nginx/html nginx`
 
- **命名卷挂载**
  - **创建挂载卷**
  `docker volume create nginx_html`
  - **查看命名挂载卷的真实目录**
  `docker volume inspect nginx_html`

- **查看创建的所有卷**
`docker volume list`

- **删除卷**
`docker volume rm volume_name`

- **删除任何容器没有在使用的卷**
`docker volume prune -a`

~~**docker run -e 环境变量**~~

**查看容器启动时携带的参数**
`docker inspect container_id`

**给容器起名**
`docker run --name my_nginx nginx`

**调试容器**
`docker run -it --rm container_name`
- `-it：`进入该容器
- `--rm：`当容器停止运行时就删除该容器

**只要容器停止就会立即重启**
`docker run -d --restart always nginx`

**手动停止的容器就不会尝试重启**
`docker run -d --restart unless-stopped nginx`

**停止运行的容器**
`docker stop container_id`

**重新启动容器**
`docker start container_id`

**查看所有容器**
`docker ps -a`

**创建容器**
`docker create images_name`

**查看容器的日志**
`docker logs container_id`

**动态查看日志**
`docker logs container_id -f`
- `-f：` --follow，追踪输出

**在运行的容器中执行linux命令**
`docker exec container_id linux_cmd`

`docker exec -it container_id /bin/sh`

**查看容器内的linux的发行版**
`cat /proc/version`

**查看docker网络模式**
`docker network list`

**创建子网**
`docker network create network1 `

**容器编排技术(docker compose)** 
```
docker compose up -d
docker compose down
docker compose stop
docker compose start
```

==标准文件名：docker-compose.yaml==

**执行非标准的yaml文件**
`docker compose -f /home/test.yaml up -d`