import re
base_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

def encode (enstr):
    istr = ''
    for x in enstr:
        if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/= ':
            istr = istr + x
        else:
            x = str(str(x).encode('utf-8')).lstrip('b\'').lstrip(' ').rstrip('\'')
            if re.search('\\\\x([0-z]{2})',x):
                x = x.replace('\\x','0x').split('0x')
                x = filter(None,x)
                for z in x:
                    z = chr(int(z,16))
                    istr = istr + z
    ostr = ''
    while istr:
        temp = istr[0:3]
        istr = istr [3:]
        tmp = ''
        for i in temp:
            t = ''.join(bin(ord(i)).replace('0b',''))
            if len(t) < 8:
                t = '0' * ( 8 - len(t) % 8 ) + t
            tmp = tmp + t
            # if len(tmp) % 6 != 0:
            #     tmp = tmp + '0' * (6 - len(tmp) % 6)
        if len(temp) < 3:
            tmp = tmp + '0' * ((3 - len(temp))* 8)
        # if len(tmp) > 24:
        #     enstr = tmp[24:] + enstr
        #     tmp = tmp[0:24]
        print(tmp,len(tmp))
        while tmp:
            bstr = tmp[0:6]
            tmp = tmp[6:]
            print(bstr)
            if bstr == '000000':
                ostr = ostr + '='
            else:
                ostr = ostr + base_str[int(bstr,2)]
    print(ostr)

def decode (destr):
    tmp = ''
    for i in destr:
        if i not in base_str:
            print('不是有效的base64字符串')
            exit(0)
    #     else:
    #         if i in '=':
    #             break
    #         else:
    #             t = ''.join(bin(ord(i)).replace('0b',''))
    #             if len(t) < 8:
    #                 t = '0' + t
    #             tmp = tmp + t
    # print(tmp + ' ' + str(len(tmp)) + ' ' + str(len(tmp) % 6),end='')