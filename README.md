## Cloudflare防火墙

>搭配Cloudflare APP使用
>
>目前仅在Ubuntu、CentOS环境下测试过，Windows暂不支持

## 简介

​		Cloudflare防火墙可以检测服务器负载，有IP封锁和Cloudflare Under Attack模式两种防御方法，有效抵挡攻击

## 安装方法

1. 打开安装目录

   ```bash
   sh install.sh
   ```

2. 等待依赖安装完成（pip3,python3的flask）

3. 根据```install.sh```安装向导完成安装

## 使用方法

1. 打开安装目录

2. 启动server.py

   ```shell
   python3 server.py
   ```

3. 服务端口为安装时输入的端口，连接密码是安装时输入的密码

#### Tip:
1. 若要开机启动请自行配置开机启动脚本，将```python3 server.py```放入
2. 防火墙日志文件在log.txt里（只有触发防火墙才会记录日志）
3. 如果无法访问服务器，请在系统防火墙放行配置的端口

> ### 使用方式
>
> 1.搭配Cloudflare APP使用
>
> 2.查看server.py有关api
---
> ### 联系方式
>
> QQ : 3319066174
>
> Email : cxbsoft@bsot.cn
>
> Github : https://github.com/cxb-soft
>
> Blog : https://blog.bsot.cn

