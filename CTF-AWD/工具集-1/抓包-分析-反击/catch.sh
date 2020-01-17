#!/usr/bin/env bash
ip=($(ifconfig -a | grep inet | grep -v 127.0.0.1 | grep -v inet6 | awk '{print $2}' | tr -d "addrs"))
eth=($(ifconfig -a | grep UP |grep flags | grep -v lo | awk '{print $1}' | tr -d ":"))
if (( ${#ip[@]} > 1 )); then
    n=1
    for x in ${ip[@]}; do
        echo $n.${eth[$n-1]}:     $x
        n=`expr $n + 1`
    done
    read -p '请输入要监听的网卡序号:' num
    while ((($num > ${#ip[@]} + 1) || $num <= 0 )); do
        read -p '请输入正确的网卡序号:' num
    done
    ip=${ip[$num-1]}
    eth=${eth[$num-1]}
fi
echo $ip
tcpdump -s 0 -i $eth -A "dst host $ip and tcp port 80 and (tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354) or tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420" -nn -X -w "$(cd "$(dirname "$0")";pwd)/catch.cap"