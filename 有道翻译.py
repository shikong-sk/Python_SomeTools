import hashlib
import time
import urllib.request
import urllib.parse
import re
import json

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

if __name__ == "__main__":
    while True:
        text = input('请输入要翻译的内容：\n')
        if text in ('quit','q','退出'):
            break
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
        heads = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
        data = createData(text)
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url=url, data=data, method='POST',headers=heads)
        response = urllib.request.urlopen(req)
        translateResult = response.read().decode('utf-8')
        target = json.loads(translateResult)
        print(target['translateResult'][0][0]['tgt'],end='\n\n')