import json
from invoke import task,run

"""
* default configure file is `config`
* `$invoke [function name] --config [configure file]`
* `invoke add_node_tags --config host_info.json`
* `invoke clean_node_tags --config host_info.json`
"""

def get_config(config):
    f = open(config)
    config = json.load(f)

    f.close()
    return config

def get_tag_name(tag):
    return tag.split("=")[0]

@task
def add_node_tags(ctx, config="config"):
    config = get_config(config)

    hosts = config["hosts"]

    for h in hosts:
        for tag in h["node-tags"]:
            #ctx.run("kubectl label node %s %s" % (h["node-name"], tag))
            print "kubectl label node %s %s" % (h["node-name"], tag)

@task
def clean_node_tags(ctx, config="config"):
    config = get_config(config)

    hosts = config["hosts"]

    for h in hosts:
        for tag in h["node-tags"]:
            tag_name = get_tag_name(tag)
            #ctx.run("kubectl label node %s %s-" % (h["node-name"], tag_name))
            print "kubectl label node %s %s- " % (h["node-name"], tag_name)

