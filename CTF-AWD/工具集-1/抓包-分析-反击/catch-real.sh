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
read -p '请输入要监听端口号:' port
while ((($port > 65535 ) || $port <= 0 )); do
    read -p '请输入正确的端口号:' port
done
# while [ condition ]; do
#     # catch=$(\
#     # tcpdump -l -c 1 -s 0 -i enp0s3 \
#     # -A "dst host 10.0.2.15 and tcp port 80 and \
#     # (tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354) or tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420" \
#     # -nn 2>&1 )
#     # echo $catch | grep 'IP'
#     cat tmp
#     # for x in ${catch[@]}; do
#     #     echo $x
#     # done
# done
# # tcpdump -l -s 0 -i enp0s3 \
# #     -A "dst host 10.0.2.15 and tcp port 80 and \
# #     (tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354) or tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420" \
# #     -nn 
# # echo $(tcpdump -l -s 0 -i enp0s3 \
# #     -A "dst host 10.0.2.15 and tcp port 80 and \
# #     (tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354) or tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420" \
# #     -nn ) | while read line
# # do
# #     echo $line
# # done
# tshark -t ad -f 'dst host 10.0.2.15 and tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -R 'http.request.method == "GET" || http.request.method == "POST"' \
# -Y 'http.request.method and http.request.uri' -T fields -e http.request.method -e http.request.uri -e text
# tshark -l -t ad -f 'dst host 10.0.2.15 and tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -R 'http.request.method == "GET" || http.request.method == "POST"' \
# -Y 'http.request.method and http.request.uri' -T fields -e text | sed 's/\\r\\n//g' | sed 's/Cache*,,//g'
# tshark -l -s 0 -t ad -f 'dst host 10.0.2.15 and tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -R 'http.request.method == "GET" || http.request.method == "POST"' \
# -Y 'http.request.method and http.request.uri' -T fields -e frame.time -e ip.src -e text | sed 's/HTTP\/1.1.*,HTTP request [0-9]*\/[0-9]*,\?/     /g' >> tmp
tshark -i $eth -l -s 0 -t ad -f "dst host $ip and tcp port $port and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)" -R 'http.request.method == "GET" || http.request.method == "POST"' \
-Y 'http.request.method and http.request.uri' -T fields -e frame.time -e ip.src -e text | tee -a catch.tmp
# while [ 1 ];do
#     data=($(tshark -c 1 -l -t ad -f 'dst host 10.0.2.15 and tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -R 'http.request.method == "GET" || http.request.method == "POST"' \
#     -Y 'http.request.method and http.request.uri' -T fields -e text | sed 's/\\r\\n//g'))
#     echo ${data[@]}
# done