#!/usr/bin/env bash
path=('/var/www' '/www/wwwroot' '/home/wwwroot')
ergodic()
{
    for file in $1/*; do
        if [ -e $file ];then
            if [ -d $file ]; then
                ergodic $file "$2"
            else
                echo `sha1sum "$file"` 1>>"$2" 2>/dev/null
            fi
        fi
    done
}
for dir in ${path[@]}; do
    if [ -e $dir ]; then
        echo "$dir 存在"
        if [ -e "root.sha" ]; then
            time=`date +'%Y-%m-%d %H_%M_%S'`
            sha="$time.sha"
            ergodic $dir "`dirname $0`/$sha"
            echo "文件效验完成 效验文件存放在 `dirname $0`/$sha"
        else
            sha="root.sha"
            ergodic $dir "`dirname $0`/$sha"
            echo "主效验文件生成完成 文件sha1主效验文件存放在 `dirname $0`/$sha" 1>&2
            exit
        fi
    else
        echo "$dir 不存在"
    fi
done
if [ -e "root.sha" ]; then
    cat root.sha > "`dirname $0`/tlog"
    cat "`dirname $0`/$sha" >> "`dirname $0`/tlog"
    sort "`dirname $0`/tlog" | uniq -u > "`dirname $0`/log"
    rm -rf "`dirname $0`/tlog"
    if (( `ls -l "$(dirname $0)/log" | awk '{print $5}'` > 0 )); then
        echo -e "\n文件效验异常，请检查下列文件是否正常：" | tee "`dirname $0`/show"
        cat "`dirname $0`/log" | tee -a "`dirname $0`/show"
    else
        echo "" 1>>"`dirname $0`/show"
    fi
fi