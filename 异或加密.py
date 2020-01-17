# import base64 as b64
#
# def xor_encrypt(tips,key):
#     ltips=len(tips)
#     lkey=len(key)
#     secret=[]
#     num=0
#     for each in tips:
#         if num>=lkey:
#             num=num%lkey
#         secret.append( chr( ord(each)^ord(key[num]) ) )
#         num+=1
#
#     return b64.b64encode( "".join( secret ).encode() ).decode()
#
#
# def xor_decrypt(secret,key):
#
#     tips = b64.b64decode( secret.encode() ).decode()
#
#     ltips=len(tips)
#     lkey=len(key)
#     secret=[]
#     num=0
#     for each in tips:
#         if num>=lkey:
#             num=num%lkey
#
#         secret.append( chr( ord(each)^ord(key[num]) ) )
#         num+=1
#
#     return "".join( secret )
#
#
# tips= "Flag.php"
# key= "AAA"
# secret = xor_encrypt(tips,key)
# print( "cipher_text:", secret )
#
# plaintxt = xor_decrypt( secret, key )
# print( "plain_text:",plaintxt )
# abc = ['f','l','a','g']
# for x in range(0,10):
#     if x ^ int(abc[0]) == oct('f'):
#         print(x)
print('flag'^'666')