from Crypto.Cipher import AES
k="7SsQWmZ524i/yVWoMeAIJA=="
k=k.decode("base64")
kirin=AES.new("weigongcun\x00\x00\x00\x00\x00\x00",AES.MODE_ECB)
print kirin.decrypt(k)
#DDCTF{Q*2!x@B0}