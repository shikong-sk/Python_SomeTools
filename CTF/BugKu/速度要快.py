import requests
import base64

url='http://123.206.87.240:8002/web6/'
s=requests.Session()
header=s.get(url).headers
#print(header)
flag = base64.b64decode(base64.b64decode(header['flag']).decode().split(':')[1]).decode() #对其进行base64两次解密

data={'margin':flag}

print(data)
print(s.post(url=url,data=data).content.decode())