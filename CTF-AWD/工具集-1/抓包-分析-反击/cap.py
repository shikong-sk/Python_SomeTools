import sys
import time 
import scapy
import chardet
from urllib import parse
from scapy.all import *
from scapy.utils import PcapReader
packets=rdpcap(sys.path[0] + "/catch.cap")
f = open(sys.path[0] + '/cap.txt','w+')
for data in packets:
    if data.haslayer("IP"):
        print('IP来源：' + data["IP"].src)
    if data.haslayer("TCP"):
        # print(data["TCP"].payload.original.decode(chardet.detect(data["TCP"].payload.original)['encoding']))
        x=data["TCP"].payload.original.decode(chardet.detect(data["TCP"].payload.original)['encoding']).split('\r\n')
        # print(x)
        t = time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(data.__dict__['time']))
        print('访问时间：' + t )
        if 'POST' in x[0]:
            print('请求类型：POST')
            print('请求页面：' + x[0][5:-9])
            print('请求内容：' + x[-1])
            f.write('Time：' + t + ' ' +'IP：' + data["IP"].src + ' ' +'Method：POST' + ' ' + 'Page：' + x[0][5:-9] + ' ' + 'Data：' + parse.quote(x[-1]) + '\n')
        else:
            print('请求类型：GET')
            print('请求页面：' + x[0][4:-9])
            f.write('Time：' + t + ' ' +'IP：' + data["IP"].src + ' ' +'Method：GET' + ' ' + 'Page：' + x[0][4:-9] + ' ' + 'Data：' + x[-1] + '\n')
    print('')
    # print(data.__dict__)
    # print(data.__dict__['original'])