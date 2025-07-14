**LVS**
- **ipvs：** 工作在内核空间，是真正实现调度的部分，由ip包处理、负载均衡算法、系统配置与管理这三个模块以及虚拟服务器与真实服务器链表组成
- **ipvsadm：** 工作在用户空间，即ipvs管理器，负责为ipvs内核编写规则，定义谁是集群服务谁是后端真实的服务器

**技术术语**
- **DS（Director Server）：** 前端负载均衡节点
- **RS（Real Server）：** 后端真实服务器
- **VIP（Virtual IP）：** 向外部直接面向用户请求，作为用户请求的目标ip
- **DIP（Director Server IP）：** 用于和内部主机通讯的ip
- **RIP（Real Server IP）：** 后端服务器的ip
- **CIP（Client IP）：** 访问客户端的ip

**LVS工作模式和原理**
- **NAT模式**
    - **原理：** 
      - 当客户端的请求到达DS也就是负载均衡节点时，请求的报文会先进入内核空间的prerouting链。此时报文的源ip为cip，目标ip为vip
      - 此时prerouting链检查数据包发现目标ip时本机便将数据包发给input链
      - ipvs也就是负责负载均衡的部分会判断请求的服务是否为集群服务，如果是它就会将数据包的目标ip修改为后端的真实ip，然后再将数据包发给postrouting链。此时报文的源ip为cip，目标ip为rip
      - postrouting链通过选路将数据包发给rs
      - rs发现目标ip是自己的就会构建响应报文发回ds。此时源ip为rip，目标ip为cip
      - ds再响应客户端之前将源ip改为自己的ip也就是vip，然后响应客户端。此时yuanip为vip,目标ip为cip
    - **特性：**
      - rip最好是内网ip
      - rs的网关必须指向dip
      - dip和rip必须再同一个网段中
      - 请求和回应的报文必须经过director，director容易称为瓶颈
      - nat支持端口转发

- **DR模式**
  - **原理：** 
    - 首先客户端使用cip请求vip
    - 当请求到达ds时，报文先进入prerouting链。此时报文的源ip为cip，目标ip为vip
    - prerouting链检查发现目标ip是本机，就将数据包发给input链
    - ipvs对比发现数据包请求的是集群服务就将报文的源mac地址改为dip的mac地址，将目标mac地址修改为rip的mac地址，然后数据包发给postrouting链，。此时源ip与目标ip均未被修改，仅修改了源mac地址为dip的mac地址，目标mac地址为rip的mac地址
    - 由于ds和rs在同一个网络下，所以通过二层来传输。postrouting链检查发现目标mac地址为rip的mac地址就将数据包发给rs
    - rs发现报文的mac地址是自己的mac地址，就接收该报文。处理完成以后就将响应报文通过lo接口传给eth0网卡然后向外发出。此时源ip为vip，目标ip为cip
    - 报文最终到达客户端
  - **配置DR**
    - **第一种：** 
    - **第二种：** 
    - **第三种：** 
  - **特性：** 