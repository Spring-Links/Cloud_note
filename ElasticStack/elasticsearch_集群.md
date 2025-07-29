**elasticsearch集群：** 由多个节点组成
**设置集群名称：** `cluster.name`
**设置节点名称：** `node.name`

**节点**
- **master：** 控制集群、创建删除索引、管理其他非master节点
- **data：** 执行与数据相关的操作，比如文档的CRUD操作
- **客户端节点：** 该节点不能作为master节点和data节点，用于响应用户请求，将请求转发到其他节点
- **部落节点：** 当一个节点配置了`tribe.*`时，它是一个特殊客户端，它可以连接多个集群，在所连接的集群上执行搜索和其他操作

**集群搭建**
- 在三台服务器中新建用户elsearch，创建/itcast/es-cluster，并赋权限，将elasticsearch文件拷贝至该目录
- 配置三台服务器的/conf/elasticsearch.yml文件
- 启动elasticsearch