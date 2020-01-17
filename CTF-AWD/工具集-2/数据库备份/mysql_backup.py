# import pexpect
import os, time

backup_path = "/root/mysql/"

# 创建备份目录~/mysql
if not os.path.exists(backup_path):

    os.makedirs(backup_path)
    print("backupdir：%s create done!，start auto backup!" %backup_path)

# try:
#    os.mkdir("~/mysql")
# except Exception as e:
#    print("目录已存在，跳过创建")

def backup_fun(db_user, db_pass, mysql_backup_path, datatime):

    get_shell_cmd = "mysqldump -u " + db_user + " -p " + db_pass + " --single-transaction --all-databases > " + mysql_backup_path
    #    print(get_shell_cmd)
    system_cmd = os.system(get_shell_cmd)
    if (len(str(system_cmd))) > 0:
        print(datatime + " " + mysql_backup_path + " backup done!")


def main():
    # 数据库账号密码
    db_user = "root"
    db_pass = "root"
    datatime = time.strftime("%H-%M-%S", time.localtime())
    backup_name = datatime + "_backup.sql"
    mysql_backup_path = backup_path + backup_name
    backup_fun(db_user, db_pass, mysql_backup_path, datatime)


if __name__ == '__main__':
    while True:
        main()
        # 定时时间为10秒备份一次
        time.sleep(10)