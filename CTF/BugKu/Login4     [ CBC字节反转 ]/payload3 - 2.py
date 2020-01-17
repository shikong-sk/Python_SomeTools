import base64
import requests
import urllib

cipher = 'qNdCkXe6Dyoeq3FNHB5hlW1lIjtzOjU6ImFkbWluIjtzOjg6InBhc3N3b3JkIjtzOjM6IjEyMyI7fQ=='#填写提交后所得的无法反序列化密文
iv = 'p8iceyrMmaxwPEJ7XpXadw%3D%3D'#一开始提交的iv

#cipher = urllib.unquote(cipher)

cipher = base64.b64decode(cipher.encode('latin-1')).decode('latin-1')
iv = base64.b64decode(urllib.parse.unquote(iv).encode('latin-1')).decode('latin-1')

newIv = ''
right = 'a:2:{s:8:"userna'#被损坏前正确的明文
for i in range(16):
    newIv += chr(ord(right[i])^ord(iv[i])^ord(cipher[i])) #这一步相当于把原来iv中不匹配的部分修改过来
print('新的IV：\n' + urllib.parse.quote(base64.b64encode(newIv.encode('latin-1')).decode('latin-1')))