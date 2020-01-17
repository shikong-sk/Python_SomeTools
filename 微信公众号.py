import itchatmp
import os
import sys
import time
import csv
import re
import hashlib
import urllib.request
import urllib.parse
import json
import chardet

itchatmp.update_config(itchatmp.WechatConfig(
    token='token', 
    appId = 'appId',
    appSecret = 'appSecret',
    encryptMode=itchatmp.content.SAFE,
    encodingAesKey='encodingAesKey'))

text = {'ToUserName': '公众号ID', 'FromUserName': '用户ID', 'CreateTime': '时间', 'MsgType': '消息类型', 'Content': '消息内容'}
whitelist = {'o6xE150NmUB1heMXnZx8uxpyViX0':'时空'}

def dataRead(userDataFile,userData):
    if not os.path.exists(userDataFile):
        userFile = open(userDataFile,'w+')
        user = dict()
    else:
        userFile = open(userDataFile,'r+')
        user = csv.reader(userFile)
    
    for x in user:
        if userData['FromUserName'] == x[0]:
            userData['FromUserName'] = x[1]
            userData['用户组'] = x[2]
            userData['积分'] = x[3]
            userFile.close()
            return userData
    userData['用户组'] = '游客'
    userData['积分'] = '0'
    return userData

def dataWrite(File,msg):
    data = {}
    for key,value in msg.items():
        if key in text.keys():
            data[text[key]] = value.encode('GBK','ignore').decode('GBK')
        else:
            data[key] = value.encode('GBK','ignore').decode('GBK')

    if not os.path.exists(File):
        fileData = open(File,'w+',newline='')
        w = csv.DictWriter(fileData,fieldnames=data.keys())
        w.writeheader()
    else:
        fileData = open(File,'a+',newline='')
        w = csv.DictWriter(fileData,fieldnames=data.keys())
    w.writerow(data)
    fileData.close()

def userManger(msg):
    msgDir = sys.path[0] + '/userMsg'
    userDir = sys.path[0] + '/userData'

    if not os.path.exists(msgDir):
        os.mkdir(msgDir)
    if not os.path.exists(userDir):
        os.mkdir(userDir)

    userDataFile = sys.path[0] + '/userData' + '/userData.csv'

    userData = dataRead(userDataFile,msg)

    if msg['FromUserName'] != userData['FromUserName']:
        if os.path.exists(sys.path[0] + '/userMsg' + '/' + msg['FromUserName'] + '.csv'):
            os.rename(sys.path[0] + '/userMsg' + '/' + msg['FromUserName'] + '.csv',sys.path[0] + '/userMsg' + '/' + userData['FromUserName'] + '.csv')
        msg['FromUserName'] = userData['FromUserName']

    userMsgFile = sys.path[0] + '/userMsg' + '/' + msg['FromUserName'] + '.csv'

    for key,value in msg.items():
        if key in text.keys():
            print(text[key] + "：" + value)
        else:
            print(key + "：" + value)

    dataWrite(userMsgFile,msg)

def createData(transStr):
    transStr = transStr.encode('utf-8')
    salt = str(int(time.time()*1000)).encode('utf-8')
    client = 'fanyideskweb'.encode('utf-8')
    a = "n%A-rKaT5fb[Gy?;N5@Tj".encode('utf-8')
    md5 = hashlib.md5()
    digStr = client+transStr+salt+a
    md5.update(digStr)
    sign = md5.hexdigest()

    data = {
        'i': transStr ,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CL1CKBUTTON',
        'typoResult': 'true'
    }
    return data
    
def translate(text):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
    heads = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
    data = createData(text)
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url=url, data=data, method='POST',headers=heads)
    response = urllib.request.urlopen(req)
    translateResult = response.read().decode('utf-8')
    target = json.loads(translateResult)
    return target['translateResult'][0][0]['tgt']

def wzryHeroData(hero):
    data = {
        '英雄': hero ,
        'sub':''
    }
    url = 'http://wzry.skcks.cn/core/post.core.php'
    heads = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url=url, data=data, method='POST',headers=heads)
    try:
        response = urllib.request.urlopen(req,timeout=3)
    except:
        return '查询超时，请稍后再试'
    translateResult = response.read().decode('utf-8')
    if translateResult:
        target = json.loads(translateResult)
        heroData = ''
        for key,value in target.items():
            if str(key) in ['攻速成长','基础暴击率','基础暴击效果']:
                value = str(float(value) * 100) + '%'
            if str(value)=='None':
                value = '无'
            heroData += str(key) + '：' + str(value) + '\n'
        return heroData.rstrip('\n')
    else:
        return '未查询到结果'
    

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    msg['CreateTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(msg['CreateTime'])))
    
    if msg['Content'] == '用户信息':
        userManger(msg)
        print()
        return '用户信息：\n' + '       用户组：' + msg['用户组'] + '\n' + '        积分：' + msg['积分']
        
    if re.search('^翻译[:： ].+?',msg['Content']):
        userManger(msg)
        print()
        return translate(re.split('^翻译[:： ]',msg['Content'],1)[1])       

    if re.search('^王者荣耀[:： ].+?',msg['Content']):
        userManger(msg)
        print()
        return wzryHeroData(re.split('^王者荣耀[:： ]',msg['Content'],1)[1])   

    if msg['FromUserName'] in whitelist.keys():
        userManger(msg)
        print()
    else:
        userManger(msg)
        print()
        return '自动回复：\n        内部测试中,公众号部分功能暂不开放'

itchatmp.run()