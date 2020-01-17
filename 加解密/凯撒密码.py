def encryption(str, n):
    cipher = []
    for i in range(len(str)):
        if str[i].islower():
            if ord(str[i]) < 123 - n:
                c = chr(ord(str[i]) + n)
                cipher.append(c)
            else:
                c = chr(ord(str[i]) + n - 26)
                cipher.append(c)
        elif str[i].isupper():
            if ord(str[i]) < 91 - n:
                c = chr(ord(str[i]) + n)
                cipher.append(c)
            else:
                c = chr(ord(str[i]) + n - 26)
                cipher.append(c)
        else:
            c = str[i]
            cipher.append(c)
    cipherstr = ('').join(cipher)
    return cipherstr

if __name__ == '__main__':
  while 1:
    print('选择你需要的功能(1.加密 2.解密 q.退出)：',end='')
    功能 = input()
    if(功能 == '1'):
      print('输入需要加密的明文：',end='')
      明文 = input()
      print('输入偏移量：',end='')
      偏移量 = int(input())
      if 偏移量>26:
          偏移量%=26
      密文 = encryption(明文, 偏移量)
      print('加密后的密文为：',end='')
      print(密文)
    elif(功能=='2'):
      print('输入需要解密的密文：',end='')
      密文 = input()
      for x in range(26):
        明文 = encryption(密文, x)
        print(明文)
    elif(功能== 'q' or 功能 == 'Q'):
      exit(0)