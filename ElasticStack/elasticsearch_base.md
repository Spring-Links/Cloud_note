### Elastic概况
- **beats：** 采集数据
  - **Packetbeat：** 监控采集网络流量信息
  - **Filebeat：** 用于监控收集服务器日志文件
  - **Metricbeat：** 定期获取外部系统的监控指标信息
  - **Winlogbeat：** 监控采集win系统的日志信息

- **elasticsearch：** 核心存储和检索引擎
- **logstash：** 高吞吐量数据处理引擎
- **kibana：** 数据可视化


**elsearch配置**
- **修改ip地址**
```
vim /conf/elasticsearch.yml
network.host: 0.0.0.0 --任意网络均可访问
```
==当network.host不是localhost或127.0.0.1时，elasticsearch就认为当前是生产环境==

- **修改jvm**
```
vim conf/jvm.options
-Xms128m
-Xmx128m
```

- **修改内存映射数量**
```
vim /etc/sysctl.conf
vm.max_map_count=655360
sysctl -p --配置生效
```
- **启动elsearch**
```
./elasticsearch
```

格式化查询结果 `?pretty`
查询部分结果 `?_source=id,name`
查询简化结果 `/_source?_source=id,name`
查询文档是否存在：使用head请求

**批量查询**
```
{
    "ids" : ["_id", "_id"]
}
```

**批量插入**
```
POST请求
URL：/itcast/_bulk
{"create":{"_index":"haoke","_type":"user","_id":"2001"}}
{"id":"2001","name":"jay","age":"22","sex":"male"}
{"create":{"_index":"haoke","_type":"user","_id":"2002"}}
{"id":"2002","name":"tom","age":"21","sex":"female"}
{"create":{"_index":"haoke","_type":"user","_id":"2003"}}
{"id":"2003","name":"monika","age":"22","sex":"male"}

```

**批量删除**
```
POST请求
URL：
{"delete":{"_index":"haoke","_type":"user","_id":"2001"}}
{"delete":{"_index":"haoke","_type":"user","_id":"2002"}}
{"delete":{"_index":"haoke","_type":"user","_id":"2003"}}
```

**分页查询**
```
GET请求
URL：
http://192.168.174.156:9200/haoke/user/_search?size=5&from=5
size：返回几条数据
from：从第几条数据开始
```

**映射**
`String : text、keyword`
`Whole number : byte、short、integer、long`
`Floating point : float、double`
`Boolean : boolean`
`Date : date`
==text：做分词，存放如邮件内容、产品描述==
==keyword：不做分词，存放如邮件地址、主机地址==

**创建明确定义字段类型的索引**
```
PUT请求
URL：/itcast
{
    "setting" : {
        "index" : {
            "number_of_shards" : "2",
            "number_of_replicas" : "0"
        }
    },
    "mappings" : {
        "person" : {
            "properties" : {
                "name" : {
                    "type" : "text"
                },
                "age" : {
                    "type" : "integer"
                },
                "mail" : {
                    "type" : "keyword"                    
                },
                "hobby" : {
                    "type" : "text"                    
                }
            }
        }
    }
}
```

**查看映射**
```
GET请求
URL：/itcast/_mapping
```

**批量插入**
```
POST请求
URL：/itcast/person/_bulk
{"index":{"_index":"itcast","_type":"person"}}
{"name":"jay","age":"22","mail":"111@qq.com","hobby":"羽毛球、乒乓球、篮球、足球"}
{"index":{"_index":"itcast","_type":"person"}}
{"name":"tom","age":"21","mail":"222@qq.com","hobby":"篮球、足球"}
{"index":{"_index":"itcast","_type":"person"}}
{"name":"monika","age":"22","mail":"333@qq.com","hobby":"乒乓球、篮球、足球"}
{"index":{"_index":"itcast","_type":"person"}}
{"name":"marry","age":"22","mail":"444@qq.com","hobby":"羽毛球、乒乓球、足球"}
{"index":{"_index":"itcast","_type":"person"}}
{"name":"robby","age":"21","mail":"555@qq.com","hobby":"乒乓球、篮球、足球"}
{"index":{"_index":"itcast","_type":"person"}}
{"name":"jim","age":"25","mail":"666@qq.com","hobby":"羽毛球、篮球、足球"}

```

**结构化查询**
- **trem查询：** 主要查询精确值，如数字、日期、布尔值
```
POST请求
URL：/itcast/person/_search
{
    "query" : {
        "term" : {
            "age" : "22"
        }
    }
}
```

- **terms查询：** 相较于term，它允许指定多个匹配条件
```
POST请求
URL：/itcast/person/_search
{
    "query" : {
        "terms" : {
            "age" : [20,21,22]
        }
    }
}
```

**range查询**
```
POST请求
URL：/itcast/person/_search
{
    "query" : {
        "range" : {
            "age" : {
                "gte" : 20,
                "lte" : 22
            }
        }
    }
}

gt：大于
gte：大于等于
lt：小于
lte：小于等于
```

**查询文档中是否包含某个字段**
```
POST请求
URL：/itcast/person/_search
{
    "query" : {
        "exists" : {
            "field" : "title"
        }        
    }

}
```

**match查询**
```
POST请求
URL：/itcast/person/_search
{
    "query" : {
        "match" : {
            "age" : "22"
        }        
    }

}
```

**bool查询**
==must：相当于and==
==must_not：相当于not==
==should：相当于or==
```
POST请求
URL：/itcast/person/_search
{
    "query" : {
        "bool" : {
            "must" : {
                "match" : {
                    "hobby" : "羽毛球"
                }
            },
            "must_not" : {
                "match" : {
                    "hobby" : "音乐"
                }
            }
        }
    }
}
```

**过滤查询：** 适合精确匹配，过滤语句可以缓存数据
```
POST请求
URL：/itcast/person/_search
{
    "query" : {
        "bool" : {
            "filter" : {
                "term" : {
                    "age" : 22
                }
            }
        }
    }
}
```

**分词（文本分析）**
```
POST请求
/_analyze
{
    "analyzer" : "standard",
    "text" : "hello word"
}
```

**中文分词（IK分词器）**
> ik插件地址：https://release.infinilabs.com/analysis-ik/stable/
> 将压缩包解压至elasearch的plugins目录下
```
POST请求
/_analyze
{
    "analyzer" : "ik_max_word",
    "text" : "我是中国人"
}
```

**非关联搜索（or）**
```
POST请求
/itcast/person/_search
{
    "query" : {
        "match" : {
            "hobby" : {
                "query" : "羽毛球 篮球"
            }
        }
    },
    "highlight" : {
        "fields" : {
            "hobby" : {}
        }
    }
}
```

**关联搜索（and）**
```
POST请求
/itcast/person/_search
{
    "query" : {
        "match" : {
            "hobby" : {
                "query" : "羽毛球 篮球",
                "operator" : "and"
            }
        }
    },
    "highlight" : {
        "fields" : {
            "hobby" : {}
        }
    }
}
```

**最小匹配度**
==百分比越高越接近and==
```
POST请求
/itcast/person/_search
{
    "query" : {
        "match" : {
            "hobby" : {
                "query" : "羽毛球 篮球",
                "minimum_should_match" : "80%"
            }
        }
    },
    "highlight" : {
        "fields" : {
            "hobby" : {}
        }
    }
}
```

**组合搜索**
```
POST请求
/itcast/person/_search
{
    "query": {
        "bool": {
            "must": {
                "match": {
                    "hobby": "篮球"
                }
            },
            "must_not": {
                "match": {
                    "hobby": "足球"
                }
            },
            "should": [{
                "match": {
                    "hobby": "乒乓球"
                }
            }]
        }
    }
}
```

**权重搜索**
```
POST请求
/itcast/person/_search
{
    "query" : {
        "bool" : {
            "must" : {
                "match" : {
                    "hobby" : {
                        "query" : "篮球",
                        "operator" : "and"
                    }
                }
            },
            "should" : [{
                "match" : {
                    "hobby" : {
                        "query" : "乒乓球",
                        "boost" : 10 
                    }
                }
            },{
                "match" : {
                    "hobby" : {
                        "query" : "羽毛球",
                        "boost" : 2
                    }
                }
            }]
        }
    },
    "highlight" : {
        "fields" : {
            "hobby" : {}
        }
    }
}
```



==elsearch报错==
> [错误一]：max file descriptors [4096] for elasticsearch process is too low, increase to at least [65536]
```
vim /etc/security/limits.conf
-- 添加如下内容：
* soft nofile 65536
* hard nofile 131072
* soft nproc 2048
* hard nproc 4096
```
> [错误二]：max number of threads [1024] for user [elsearch] is too low, increase to at least [4096]
```
vim /etc/security/limits.d/90-nproc.conf
-- 修改配置值
* soft nproc 4096
```
> [错误三]：system call filters failed to install; check the logs and fix your configuration or disable system call filters at your own risk
```
vim config/elasticsearch.yml
-- 添加如下内容：
bootstrap.system_call_filter: false
```




```
{
    "query" : {
        "match": {
            "age" : 21
        }
    }
}

{
    "id":"1001",
    "name":"张三",
    "age":"20",
    "sex":"男"
}

{
    "query" : {
        "bool": {
            "filter" : {
                "range" : {
                    "age" : {
                        "gt" : "30"
                    }
                }
            },
            "must" : {
                "match" : {
                    "id" : "1005"
                }
            }
        }
    }
}

{
    "query" : {
        "match": {
            "name" : "张三 李四" 
        }
    },
    "highlight" : {
        "fields" : {
            "name" : {}
        }
    }
}

{
    "aggs" : {
        "all_interests" : {
            "terms" : {
                "field" : "age"
            }
        }
    }
}
```
