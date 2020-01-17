# Author:Shikong
def Caser(x,key):
    w = ''
    if key > 26 or key < -26:
        key %= 26
    for t in x:
        if t.islower():
            s = ord(t)+key
            if s > 122:
                s -= 26
            if s < 97:
                s += 26
            t = chr(s)
        if t.isupper():
            s = ord(t)+key
            if s > 90:
                s -= 26
            if s < 65:
                s += 26
            t = chr(s)
        w += t       
    return w

if __name__ == '__main__':
    while 1:
        while 1:
            inp = None
            try:
                inp = int(input('请选择要运行的功能  \n 1.加密 \n 2.解密 \n 0.退出 \n'))
            except:
                print('请输入正确的参数')
            else:
                break
        if inp == 1:
            x = input('输入要加密的内容：')
            while 1:
                key = None
                try:
                    key = int(input('请输入key值：'))
                except:
                    print('请输入数字')
                else:
                    break
            print(Caser(x,key))
        if inp == 2:
            x = input('输入要解密的内容：')
            for key in range(26):
                print(Caser(x,key))
        if inp == 0:
            exit(0)
