# !/var/bin python
#coding=utf-8

import pexpect

def ssh_copy_fun(ssh_ip, ssh_user, ssh_passwd, default_copy_dir, copy_dir,local_ip, local_passwd):
    ssh_get_cmd = "ssh " + ssh_user + "@" + ssh_ip

    child = pexpect.spawn(ssh_get_cmd)
    fout = file('mylog.txt', 'w')
    child.logfile = fout
    try:
        child.expect("?")
        child.sendline("yes")
    except:
        pass
    # 输入远程PC密码登录
    child.expect("password:")
    child.sendline(ssh_passwd)


    # 让远程PC拷贝目录传给自己
    child.expect("#")
    # 判断是否指定拷贝目录，如果没有默认拷贝/var/www
    print("\n")
    if len(copy_dir)>1:
        # 打包要传输的文件夹
        ssh_tar_cmd = "tar -zcvf " +  copy_dir + ".tar.gz " + copy_dir
        print("正在将"+ copy_dir+"目录打包并压缩到"+ copy_dir+"目录, 新文件名为："+ copy_dir + ".tar.gz")
        # 传输文件
        scp_cmd = "scp " + copy_dir + ".tar.gz" + " root@" + local_ip + ":~/"

    else:
        ssh_tar_cmd = "tar -zcvf /var/www.tar.gz /var/www/"
        print("正在将/var/www目录打包并压缩到/var目录, 新文件名为：www.tar.gz")
        scp_cmd = "scp /var/www.tar.gz root@" + local_ip + ":~/"
    # 执行打包命令
    child.sendline(ssh_tar_cmd)

    print("=" * 15 + "打包并压缩成功" + "=" * 15)

    # 传输文件
    print("\n")
    child.expect("#")
    child.sendline(scp_cmd)
    if len(copy_dir)>1:
        print("正在将"+ copy_dir +".tar.gz文件拷贝到本机的~/目录")
    else:
        print("正在将/var/www.tar.gz文件拷贝到本机的~/目录")
    print("=" * 15 + "传输成功" + "=" * 15)

    try:
        # 如果是第一次copy的话，需要输入yes
        child.expect("?")
        child.sendline("yes")
    except:
        pass
    child.expect("password:")
    child.sendline(local_passwd)
    child.expect("#")
    child.sendline("exit")
    print("\n")
    if len(copy_dir)>1:
        print("成功拷贝" + ssh_ip + "的"+ copy_dir +"目录到本机的" + "~/目录")
    else:
        print("成功拷贝" + ssh_ip + "的/var/www目录到本机的" + "~/目录")
def main():
    ssh_ip = "192.168.1.15"
    ssh_user = "root"
    ssh_passwd = "centos"
    default_copy_dir = "/var/www"
    # copy_dir = ""
    local_ip = "192.168.1.4"
    local_passwd = "toor"
    # local_ip = raw_input("请输入本机IP：")
    # local_passwd = raw_input("请输入本机密码：")
    # ssh_ip = raw_input("请输入SSH远程IP：")
    # ssh_user = raw_input("请输入SSH账号：")
    # ssh_passwd = raw_input("请输入SSH密码：")
    # 默认拷贝目录
    default_copy_dir = "/var/www"
    copy_dir = raw_input("请输入拷贝目录，不输入默认拷贝本机的/var/www目录：")
    if len(copy_dir) >1 :
        print("开始对" + ssh_ip + "的" + copy_dir + "目录进行拷贝！")
    else:
        print("开始对" + ssh_ip + "的/var/www目录进行拷贝！")
    ssh_copy_fun(ssh_ip, ssh_user, ssh_passwd, default_copy_dir, copy_dir,local_ip, local_passwd)

if __name__ == '__main__':
    main()

