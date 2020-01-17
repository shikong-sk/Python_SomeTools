#!/usr/bin/env bash
while [ 1 ]; do
    clear
    if [ -f "`dirname $0`/access_log/access.log" ]; then
        echo '网站访问日志（显示最后15条记录）：'
        tail -n 15 "`dirname $0`/access_log/access.log" | awk '{print $1,$4,$6,$7,$9,$10}'
    else
        echo 'access日志未配置完成'
        exit
    fi
    sleep 0.5
done