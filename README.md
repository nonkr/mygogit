# gogit

> 一个结合crontab定时推送github或coding库小玩意。

注：运行此玩意的电脑，必须可运行python、已经配置好github和coding使用ssh key 无密钥通道git的ssh获取方式(推荐使用常年不关机的linux服务器)。

配置参考：[Git配置安装使用教程操作github上传克隆数据](http://www.cnblogs.com/havenshen/p/3493522.html)

## 安装

1.克隆此库
  
  ```shell
  git clone git@github.com:HavenShen/gogit.git
  ```
  
## 配置推送github同时提交coding库

1.在自己的github和coding中创建自己的新库

  可取名如：`mygogit`取得自己的ssh地址
  
  * `git@github.com:xxx/mygogit.git`
  * `git@git.coding.net:xxx/mygogit.git`

2.修改及增加刚在github克隆的库目录下`gogit/.git/config`文件中的`[remote "origin]"`节点下`url`路径

```shell
url = git@github.com:xxx/mygogit.git
url = git@git.coding.net:xxx/mygogit.git
```

## 设置`crontab`定时任务

```shell

#编辑定时任务

crontab -e

#键入每天下午3点执行命令

00 15 * * * python /home/gitfile/gogit/main.py #这边执行路径按自己的库目录而改动

#保存退出

:wq
  
```

搞定。

坐等任务每天帮你填补github空地，以及coding每天推送代码的 + 0.01码币

## 错误反馈

1.如果crontab不执行python脚本

在`main.py`文件头部加入
  
```shell
#!/usr/bin/python #对应python环境变量路径
```
  
把Python（`main.py`）的属性改为可执行

```shell
chmod a+x main.py
```

修改`crontab`

```shell
crontab -e
00 15 * * * /home/gitfile/gogit/main.py
```
  
## License

MIT
