# python2
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import requests
import urllib
iv_raw='%2F8iEm4jh%2BjbgVGwlQ31ycg%3D%3D'
cipher_raw='8WdhbPxjZy9xYAgoCeghiOUQu0ri1Y3dv7cX44MbvOfIC6zZxCbR%2FPFpeMatL5qIgT%2BYA66tIdCBpxtWsWxV9Q%3D%3D'
print "[*]iv And cipher"
print "iv_raw:  " + iv_raw
print "cipher_raw:  " + cipher_raw
print "[*]cipher Decode"
cipher = base64.b64decode(urllib.unquote(cipher_raw))
print type(cipher)
print cipher[9]
#a:2:{s:8:"username";s:5:"zdmin";s:8:"password";s:5:"12345"}
#s:2:{s:8:"userna
#me";s:5:"zdmin";
#s:8:"password";s
#:3:"12345";}
xor_cipher = cipher[0:9] +  chr(ord(cipher[9]) ^ ord('z') ^ ord('a')) + cipher[10:]
print type(xor_cipher)
xor_cipher=urllib.quote(base64.b64encode(xor_cipher))
print "Reverse cipher:" + xor_cipher
