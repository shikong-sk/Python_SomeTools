# <center>Kali各种命令</center>

#### SSH
开机自动启动ssh：`systemctl enable ssh`
启动ssh服务：`systemctl start ssh`

> Root密码登录SSH
> `修改 /etc/ssh/sshd_config 配置文件`
>> `修改文件中的 PermitRootLogin no 为 PermitRootLogin yes 并删除开头的#，若没有此行则手动添加`
>> `修改文件中的 PasswordAuthentication no 为 PasswordAuthentication yes 并删除开头的#`

#### 网络
查看网卡配置：`ifconfig`
查看路由：`route`
重启网络：`systemctl restart networking`

#### 计算字符 MD5

`echo -n 'QNKCDZO' | md5sum | awk '{print $1}'`

#### 截取字符串 第1~2个字符

`cut -b 1,2`

#### 查找含有某字符串的文件

`grep -rn 'root' ~`

#### sqlmap (爆数据库工具)

`sqlmap -u 链接地址 [参数]`
> `--batch 全部使用默认选项，无需用户交互`
> `--dbs 爆数据库`
> `--tables 爆表名`
> `--column 爆列名`
> `-D 指定数据库名`
> `-T 指定表名`
> `-C 指定列名`
>
> `--technique [方法] 注入方法`
>> `B Boolean-based-blind（布尔型型注入）`
>> `E Error-based   （报错型注入）`
>> `U Union query-based  （联合注入）`
>> `T Time-based blind  （基于时间延迟注入）`
>> `S Starked queries   （通过sqlmap读取文件系统、操作系统、注册表必须 使用该参数，可多语句查询注入）`
>
> `--dump dump 数据库数据`
> `--threads 3 使用多线程爆破`
> `--method POST --data "id=1" 使用POST方法提交(--data 后为传递的参数)`
> `--cookie --data "id=1" 使用Cookie方式提交(--data 后为传递的参数)`
> `--referer "http://www.google.com" 伪造请求来源`
> `--current-db 获取当前数据库名称`
> `--current-user 获取当前数据库用户名称`
> `--os-cmd=whoami 执行系统命令`

#### weevely （一句话木马生成/连接工具）
> 生成一句话木马
> `weevely generate [密码] [生成路径]`

> 连接一句话木马
> `weevely [连接地址] [连接密码]`

> 恢复会话
> `weevely session [会话保存路径]`

