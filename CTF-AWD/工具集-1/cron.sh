#!/usr/bin/env bash
lang=`locale -a | grep -c zh_CN`
cron=('backup.sh' 'file.sh')
if [ ! -e "cron.lock" ]; then
    for code in ${cron[@]}; do
        if [ -f $code ]; then
            if (( $lang != 0 )); then
                echo -e "存在 \t$code\t\c"
                chmod +x `pwd`/$code
                (crontab -l | grep -v "`pwd`/$code" ; echo "*/1 * * * * bash `pwd`/$code") | crontab -u `whoami` - > /dev/null
                echo -e "\t添加并执行 $code"
                bash `pwd`/$code 1 > /dev/null
            else
                echo -e "exist \t$code\t\c"
                (crontab -l | grep -v "`pwd`/$code" ; echo "*/1 * * * * bash `pwd`/$code") | crontab -u `whoami` - > /dev/null
                echo -e "\tadd cron and execute $code"
                bash `pwd`/$code 1 > /dev/null
            fi
        else
            if (( $lang != 0 )); then
                echo -e "不存在 \t$code"
            else
                echo -e "no exist \t$code"
            fi
        fi
    done
    if (( $lang != 0 )); then
        echo -e "\n任务列表："
        crontab -l
        echo ""
        touch cron.lock
        echo "脚本已锁定，再次运行可删除已添加的任务"
        echo "如需重新添加定时任务请删除`pwd`/cron.lock 后重新运行本脚本"
    else
        echo -e "\nCron list:"
        crontab -l
        echo ""
        touch cron.lock
        echo "script is locked"
        echo "Remove `pwd`/cron.lock and rerun the script if you need to re-add cron"
    fi
else
    for code in ${cron[@]}; do
        if [ -f $code ]; then
            if (( $lang != 0 )); then
                echo -e "存在 \t$code\t\c"
                (crontab -l | grep -v "`pwd`/$code") | crontab -u `whoami` - > /dev/null
                echo -e "\t删除 $code 相应任务"
            else
                echo -e "exist \t$code\t\c"
                (crontab -l | grep -v "`pwd`/$code") | crontab -u `whoami` - > /dev/null
                echo -e "\tRemove $code cron"
            fi
        else
            if (( $lang != 0 )); then
                echo -e "不存在 \t$code"
            else
                echo -e "no exist \t$code"
            fi
        fi
    done
    if (( $lang != 0 )); then
        echo -e "\n任务列表："
        crontab -l
        rm -rf `pwd`/cron.lock
        echo "相应的定时任务已删除"
        echo "cron.lock已删除，脚本锁定解除"
    else
        echo -e "\nCron list："
        crontab -l
        rm -rf `pwd`/cron.lock
        echo "The corresponding cron has been removed"
        echo "Cron.lock has been removed"
    fi
fi