import os
import sys
import csv
import time
import re
import wordcloud
import jieba

# times = '1546079693000'
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(times)/1000)))
# select msgId 消息id,msgSvrId 不知道干啥用,Type 消息类型,status 不懂,isSend  是否是发送消息，0是接收的，1是发送的,isShowTimer 没研究,talker 对话者,imgPath 图片路径, datetime((select createTime/1000 from message b where b.msgId  = a.msgId),'unixepoch','localtime') 发送时间,content 消息内容（最主要的）,reserved 备注 from message a order by a.createtime asc ;

def dataRead(userDataFile):
    if not os.path.exists(userDataFile):
        userFile = open(userDataFile,'w+')
        user = dict()
    else:
        userFile = open(userDataFile,'r+',encoding='ISO-8859-1')
        user = csv.DictReader(userFile)
    
    userFile.close
    return user

def dataToWordCloud(data,search):
    talkData = ''
    i = 0
    for message in data:
        if i <= 0:
            i+=1
            continue

        if (message['talker'] == search and message['isSend'] == '0') or (message['talker'] == search and search == myId):
            # print('第'+str(i)+'条信息：')
            try:
                message['content'] = message['content'].encode('ISO-8859-1').decode('gbk')
            except:
                # message['content'] = message['content'].encode('utf-8').decode('utf-8')
                message['content'] = '[消息中含有无法识别的emoji字符]'

            if re.search('@chatroom$',message['talker']):
                if message['talker'] in user.keys():
                    message['talker'] = user[message['talker']]

                message['session'] = message['talker']

                if re.search('^.*?[:].*?',message['content']):
                    talker = re.split('[:]',message['content'],1)
                    if talker[0] in user.keys():
                        message['session'] = user[talker[0]]
                    else:
                        message['session'] = talker[0] 
                    message['content'] = talker[1]
                else:
                    message['session'] = my
                    message['content'] = message['content']
            else:
                if message['talker'] in user.keys():
                    message['talker'] = user[message['talker']]

                if message['isSend'] == '1':
                    message['session'] = my
                else:
                    message['session'] = message['talker']
            
            # i+=1

            if search in message['content']:
                continue

            if '[消息中含有无法识别的emoji字符]' in message['content']:
                continue

            if '<msg>' in message['content']:
                continue

            if '撤回' in message['content']:
                continue

            if 'SystemMessages' in message['content']:
                continue

            if 'voip_content_voice' in message['content']:
                continue

            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(message['createTime'])/1000)))
            print('会话_'+message['talker'],message['session'] + '：\n' +message['content'],end='\n\n')

            message['content'] = re.sub('\[.{1,2}\]','',message['content'])
            talkData += ' '.join(jieba.cut(message['content']))
            
        else:
            i+=1
            continue
    if talkData == '':
        print('未查询到ID为：' + search + '的数据')
    else:
        w = wordcloud.WordCloud(width=3000,height=1500,max_words=300,font_path="C:\Windows\Fonts\微软雅黑\msyh.ttc")
        w.generate(talkData)
        w.to_file(sys.path[0] + '/' + search +'.png')

def dataToWordCloudAll(data,search):
    talkData = ''
    i = 0

    # if search == my:
    #     search = ''

    for message in data:
        if i <= 0:
            i+=1
            continue
        # if i > 1500:
        #     exit(-1)
        i+=1
        try:
            message['content'] = message['content'].encode('ISO-8859-1').decode('gbk')
        except:
            # message['content'] = message['content'].encode('utf-8').decode('utf-8')
            message['content'] = '[消息中含有无法识别的emoji字符]'

        if message['type'] != '1' :
            continue

        if re.search('@chatroom$',message['talker']):
            if message['talker'] in user.keys():
                message['talker'] = user[message['talker']]

            message['session'] = message['talker']

            if re.search('^.*?[:].*?',message['content']):
                talker = re.split('[:]',message['content'],1)

                if talker[0] != search:
                    continue

                if talker[0] in user.keys():
                    message['session'] = user[talker[0]]
                else:
                    message['session'] = talker[0] 
                message['content'] = talker[1]
            else:
                if search == myId:
                    message['session'] = my
                    message['content'] = message['content']
                else:
                    continue

        else:
            if message['isSend'] == '1' and search != myId:
                continue

            if message['talker'] != search:
                if search == myId:
                    if message['isSend'] == '0':
                        continue
                else:
                    continue

            if message['talker'] in user.keys():
                message['talker'] = user[message['talker']]

            if message['isSend'] == '1':
                message['session'] = my
            else:
                message['session'] = message['talker']

        if '[消息中含有无法识别的emoji字符]' in message['content']:
            continue

        if '<msg>' in message['content']:
            continue

        if '撤回' in message['content']:
            continue

        if 'SystemMessages' in message['content']:
            continue

        if 'voip_content_voice' in message['content']:
            continue

        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(message['createTime'])/1000)))
        print('会话_'+message['talker'],message['session'] + '：\n' +message['content'],end='\n\n')

        message['content'] = re.sub('\[.{1,2}\]','',message['content'])
        talkData += ' '.join(jieba.cut(message['content']))
            
    if talkData == '':
        print('未查询到ID为：' + search + '的数据')
    else:
        w = wordcloud.WordCloud(width=3000,height=1500,max_words=300,font_path="C:\Windows\Fonts\微软雅黑\msyh.ttc")
        w.generate(talkData)
        w.to_file(sys.path[0] + '/' + search +'_ALL.png')
        pass

def dataSearch(data,search):
    talkData = ''
    i = 0
    for message in data:
        if i <= 0:
            i+=1
            continue

        try:
            message['content'] = message['content'].encode('ISO-8859-1').decode('gbk')
        except:
            # message['content'] = message['content'].encode('utf-8').decode('utf-8')
            message['content'] = '[消息中含有无法识别的emoji字符]'

        if message['content'] == '':
            i+=1
            continue

        if message['talker'] in message['content']:
            i+=1
            continue

        if myId in message['content']:
            i+=1
            continue

        if message['talker'] == search:
            if re.search('@chatroom$',message['talker']):
                if message['talker'] in user.keys():
                    message['talker'] = user[message['talker']]

                message['session'] = message['talker']

                if re.search('^.*?[:].*?',message['content']):
                    talker = re.split('[:]',message['content'],1)
                    if talker[0] in user.keys():
                        message['session'] = user[talker[0]]
                    else:
                        message['session'] = talker[0] 
                    message['content'] = talker[1]
                else:
                    message['session'] = my
                    message['content'] = message['content']
            else:
                if message['talker'] in user.keys():
                    message['talker'] = user[message['talker']]

                if message['isSend'] == '1':
                    message['session'] = my
                else:
                    message['session'] = message['talker']

            if search in message['content']:
                i+=1
                continue

            if '[消息中含有无法识别的emoji字符]' in message['content']:
                i+=1
                continue

            if '<msg>' in message['content']:
                i+=1
                continue

            if '撤回' in message['content']:
                i+=1
                continue

            if 'SystemMessages' in message['content']:
                i+=1
                continue

            if 'voip_content_voice' in message['content']:
                i+=1
                continue

            print('第'+str(i)+'条信息：')
            i+=1
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(message['createTime'])/1000)))
            print('会话_'+message['talker'],message['session'] + '：\n' +message['content'],end='\n\n')
            
        else:
            i+=1
            continue

def dataShow(data):
    talkData = ''
    i = 0
    for message in data:
        if i <= 0:
            i+=1
            continue

        try:
           message['content'] = message['content'].encode('ISO-8859-1').decode('gbk')
        except:
            # message['content'] = message['content'].encode('utf-8').decode('utf-8')
            message['content'] = '[消息中含有无法识别的emoji字符]'

        if message['type'] != '1' :
            i+=1
            continue

        if message['content'] == '':
            i+=1
            continue

        if message['talker'] in message['content']:
            i+=1
            continue

        if myId in message['content']:
            i+=1
            continue

        if re.search('@chatroom$',message['talker']):
            if message['talker'] in user.keys():
                message['talker'] = user[message['talker']]

            message['session'] = message['talker']

            if re.search('^.*?[:].*?',message['content']):
                talker = re.split('[:]',message['content'],1)
                if talker[0] in user.keys():
                    message['session'] = user[talker[0]]                    
                else:
                    message['session'] = talker[0] 
                message['content'] = talker[1]
            else:
                message['session'] = my
                message['content'] = message['content']
        else:                
            if message['talker'] in user.keys():
                message['talker'] = user[message['talker']]

            if message['isSend'] == '1':
                message['session'] = my
            else:
                message['session'] = message['talker']

        if '[消息中含有无法识别的emoji字符]' in message['content']:
            i+=1
            continue

        if '<msg>' in message['content']:
            i+=1
            continue

        if '撤回' in message['content']:
            i+=1
            continue

        if 'SystemMessages' in message['content']:
            i+=1
            continue

        if 'voip_content_voice' in message['content']:
            i+=1
            continue
        print('第'+str(i)+'条信息：')
        i+=1
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(message['createTime'])/1000)))
        print('会话_'+message['talker'],message['session'] + '：\n' +message['content'],end='\n\n')

my = '时空'
myId = 'zhxb919411476'

user = {
    'weixin':'微信团队',
    'zhxb919411476':'时空',
    'wxid_9pzwu6ui8h8r22':'赵丽璇',
    'wxid_6iq9w70cnagp12':'李烽楷',
    'wxid_zyf448d5q2r222':'陈弘杰',
    'wxid_s14ph6kf077v22':'李燕',
    'wxid_7uz7xxp1n7r221':'黄越',
    'wxid_awx4lyx67ory21':'曾晓莎',
    'wxid_46jc8cm49p2i22':'涂燕娜',
    'wxid_vrpbvkg3tv3r22':'邱伟鑫',
    'wxid_40bd4bli4ag922':'郑冰峰',
    'wxid_p6zqy4ovebm841':'刘辉',
    '5035977589@chatroom':'群聊_nonexistent',
    '10971171670@chatroom':'群聊_半人半狗401',
    '5783134408@chatroom':'群聊_17计应一班',
}

searchId = 'zhxb919411476'
wxData = dataRead('E:/$微信记录/2019.08.14/190814.csv')
dataToWordCloudAll(wxData,searchId)
# dataSearch(data,searchId)
# dataShow(data)