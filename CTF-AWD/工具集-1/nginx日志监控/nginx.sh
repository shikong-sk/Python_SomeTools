#!/usr/bin/env bash
nginx=('/usr/local/nginx/conf/nginx.conf' '/www/server/nginx/conf/nginx.conf')
# nginx=('/root/shell/nginx.conf')
for conf in ${nginx[@]}; do
    if [ -e "$conf" ]; then
        log=$(echo `nl $conf | sed -n '/access_log\s*off/p' | awk '{print $1}' `)
        if (( ${#log} < 0 )); then
            echo 'nginx访问日志已开启'
            echo '正在修改nginx访问日志设置'
        else
            echo '正在开启和设置nginx访问日志'
        fi

        # if [ `whoami` = 'root' ]; then
            if [ ! -e "`dirname $0`/access_log" ]; then
                mkdir `dirname $0`/access_log               
            fi
            if [ ! -f "`dirname $0`/access_log/access.log" ]; then
                touch `dirname $0`/access_log/access.log
            fi 
            sed -i 's/access_log\s*off/access_log on/g' $conf
            x=(`sed -n '/log_format.*;/p' $conf`)
            if (( ${#x} == 0 )); then
                 sed -i '/gzip_disable*/a log_format ssskkk "$remote_addr - $remote_user [$time_local] $request $request_body $status $body_bytes_sent $http_referer $http_user_agent $http_x_forwarded_for";' $conf
            else
                 sed -i 's/log_format.*;/log_format ssskkk "$remote_addr - $remote_user [$time_local] $request $request_body $status $body_bytes_sent $http_referer $http_user_agent $http_x_forwarded_for";/g' $conf
            fi
            x=$(echo "$(cd "$(dirname "$0")"; pwd)/access_log/access.log" | sed 's/\//\\\//g')
            sed -i "s/access_log.*[/].*;/access_log $x ssskkk;/g" $conf
        # fi
        echo '正在重启nginx'
        lnmp restart 1>/dev/null
        echo '操作完成'
        exit
    fi
done