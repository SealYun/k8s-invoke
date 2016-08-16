default configure file is `config`
```bash
$ invoke add_node_tags --config host_info.json
$ invoke clean_node_tags --config host_info.json
```
```bash
$ invoke --list
Available tasks:

  add_node_tags
  clean_node_tags
  
```

通过运行不同的配置文件实现弹性调度

看两个配置文件：`before_scale.json`:
```bash
{
    "hosts":[
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=ats"]
        },
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=ats"]
        },
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=ats"]
        },
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=hadoop"]
        }
    ]
}
```
after_scale.json
```bash
{
    "hosts":[
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=ats"]
        },
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=hadoop"]
        },
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=hadoop"]
        },
        {
            "node-name":"dev-1-109",
            "node-tags":["role=scale", "app=hadoop"]
        }
    ]
}
```
执行  `$ invoke add_node_tags --config before_scale.json` 即运行了三个ats 一个hadoop

弹性伸缩时 执行 `$ invoke update_node_tags --config after_scale.json` 即运行三个hadoop 一个ats
