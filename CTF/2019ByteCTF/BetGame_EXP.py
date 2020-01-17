import os
import time
import re
import socket

import socket
target_host = "112.125.25.81"
target_port = 9999
#建立socket对象,建立包含AF_INET,和SOCK_STREAM参数的socket对象。AF_INET参数锁门我们使用IPV4地址，SOCK_STREAM说明这是一个TCP客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#连接客户端
client.connect((target_host, target_port))

p = {
    'j':'j',
    's':'s',
    'b':'b'
}
lost = {
    'j':'b',
    's':'j',
    'b':'s'
}
win = {
    'j':'s',
    's':'b',
    'b':'j'
}

#get some data
response = str(client.recv(4096), encoding="utf-8")
print(response)
# response = str(client.recv(4096), encoding="utf-8")
# print(response)
# request = re.findall('I will use: (.)',response)
# if request != []:
#     client.send(bytes(request[0], encoding="utf8"))
#     print(request[0])

for x in range(31):
    response = str(client.recv(4096), encoding="utf-8")
    print(response)
    print('第'+ str(x+1) +'次')
    request = re.findall('I will use: (.)',response)
    if x %3 == 0:
        if request != []:
            client.send(bytes(p[request[0]], encoding="utf8"))
            print(p[request[0]])

    if x %3 == 1:
        if request != []:
            client.send(bytes(lost[request[0]], encoding="utf8"))
            print(lost[request[0]])

    if x %3 == 2:
        if request != []:
            client.send(bytes(win[request[0]], encoding="utf8"))
            print(win[request[0]])
    
    time.sleep(0.5)

response = str(client.recv(4096), encoding="utf-8")
print(response)





















# cmd = 'cmd.exe E:/$Python/netcat-win32-1.12/nc.exe 112.125.25.81 9999'
# cmd = 'cmd.exe'
# r = subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
# r.stdin.write('E:/$Python/netcat-win32-1.12/nc.exe 112.125.25.81 9999\r\n'.encode('GBK'))
# r.stdin.flush()
# print(r.stdout.readline().decode('GBK'))
# print(r.stdout.readline().decode('GBK'))
# print(r.stdout.readline().decode('GBK'))
# print(r.stdout.readline().decode('GBK'))
# time.sleep(1)
# print(r.stdout.readline().decode('GBK'))
# print('ready')
# for x in range(31):
#     r.stdin.write('j\r\n'.encode('GBK'))
#     r.stdin.flush()
#     print('j')
# r.stdin.write('exit\r\n'.encode('GBK'))
# r.stdin.flush()
# while True:
#     e = r.stderr.readline()
#     if e:
#         line = e
#     else:
#         line = r.stdout.readline()
#     if not line:
#         exit(0)
#     print(line.decode('GBK'))
#     # time.sleep(0.2)