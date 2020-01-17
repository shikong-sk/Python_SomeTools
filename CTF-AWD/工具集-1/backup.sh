#!/usr/bin/env bash
path=('/var/www' '/www/wwwroot' '/home/wwwroot')
for dir in ${path[@]}; do
    if [ -e $dir ]; then
        echo "$dir 存在"
        time=`date +'%Y-%m-%d %H_%M_%S'`
        backup="$dir/../$time.zip"
        zip -r "$backup" $dir 1 > /dev/null
        echo "目录：$dir 备份完成"
        echo "备份文件路径：$backup"
    else
        echo "$dir 不存在"
    fi
done