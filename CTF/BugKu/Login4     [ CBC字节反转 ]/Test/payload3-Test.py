import base64
import requests
import urllib

import re
import chardet

iv_raw='p8iceyrMmaxwPEJ7XpXadw%3D%3D'  #这里填写第一次返回的iv值
cipher_raw='L%2FI23d511PucpbfqPsb8M4tis1VekaJj0bGOY4QE86GYXQTg5NYlDF6AnqcU3K5WBiz6A7JEVvB%2BEU1HpZ9e%2BQ%3D%3D'  #这里填写第一次返回的cipher值
print("[*]原始iv和cipher\n")

print("iv_raw:  \n" + iv_raw + '\n')

print("cipher_raw:  \n" + cipher_raw + '\n')

print("[*]对cipher解码，进行反转\n")

class Code:

    @classmethod
    def getCode(cls,data):
        if(type(data) != bytes):
            data = data.encode()
        return chardet.detect(data)['encoding'] if chardet.detect(data)['encoding'] != None and chardet.detect(data)['encoding'] != 'ascii' else 'ISO-8859-1'

    @classmethod
    def b64decode(cls,data):
        return base64.b64decode(data.encode(cls.getCode(data)))

    @classmethod
    def b64encode(cls,data):
        if(type(data) != bytes):
            data = data.encode()
        return base64.b64encode(data)

    @classmethod
    def unquote(cls,data):
        return urllib.parse.unquote(data)

    @classmethod
    def quote(cls,data):
        return urllib.parse.quote(data)

def getCode(data):
    if(type(data) != bytes):
        data = data.encode()
    return chardet.detect(data)['encoding'] if chardet.detect(data)['encoding'] != None and chardet.detect(data)['encoding'] != 'ascii' else 'ISO-8859-1'



# exit()

cipher_raw = urllib.parse.unquote(cipher_raw)

# print(Code.getCode(cipher_raw))

# print(Code.b64decode(cipher_raw))

# print(Code.b64encode(Code.b64decode(cipher_raw).decode('ISO-8859-1')))

# print(Code.quote('12321321313=/-+'))

b64_cipher_raw = base64.b64decode(cipher_raw.encode(getCode(cipher_raw)))

# print(Code.getCode(b64_cipher_raw))

cipher = b64_cipher_raw.decode(getCode(b64_cipher_raw))

# print(getCode(urllib.parse.unquote(cipher_raw).encode()))

#a:2:{s:8:"username";s:5:"zdmin";s:8:"password";s:5:"12345"}
#a:2:{s:8:"userna
#me";s:5:"zdmin";
#s:8:"password";s
#:3:"12345";}

#a:2:{s:8:"username";s:5:"admik";s:8:"password";s:5:"12345"}
#a:2:{s:8:"userna
#me";s:5:"admik";
#s:8:"password";s
#:3:"12345";}

# exit()

xor_cipher = cipher[0:13] +  chr(ord(cipher[13]) ^ ord('k') ^ ord('n')) + cipher[14:]  #请根据你的输入自行更改，原理看上面的介绍

xor_cipher=urllib.parse.quote(base64.b64encode(xor_cipher.encode('latin-1')).decode('latin-1'))

print("反转后的cipher：\n" + xor_cipher)