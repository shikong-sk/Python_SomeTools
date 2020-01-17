#!/usr/bin/env bash
while [ 1 ]; do
    echo `date +'%Y-%m-%d %H_%M_%S'`
    if [ -f "`dirname $0`/show" ]; then
        cat "`dirname $0`/show" | tee -a "`dirname $0`/show.log"
    fi
    sleep 30s
done