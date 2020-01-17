import requests
# import re
import os

header = {'content-type': 'application/json',
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
          "Connection": "keep-alive",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Accept-Language": "zh-CN,zh;q=0.8",
        "Referer":"https://720yun.com/t/1fd2fxr8utr?scene_id=1158032",
        "Origin":"https://720yun.com"
          }
slist = {'b','d','f','l','r','u'}
resutle = []
url = ''
for sk in slist:
    for x in range(1,5 + 1):
        for y in range(1, 10 + 1):
            for z in range(1, 10 + 1):
                url = 'https://ssl-panoimg8.720static.com/resource/prod/69ai37767n4/6a62exikyts/975317/imgs/'+sk+'/l'+str(x)+'/0'+str(y)+'/l'+str(x)+'_'+sk+'_0'+str(y)+'_0'+str(z)+'.jpg'
                response = requests.get(url, headers=header)
                if(response.status_code != 404 or response.status_code == 200 or response.status_code == 304 ):
                    resutle.append(url)

print(resutle)

def get_web(url, fname):
    r = requests.get(url, headers=header)
    data = r.content
    with open(fname, 'wb') as fobj:
        fobj.write(data)
    return fname

pic_dir = 'C:/Users/Shikong/Desktop/666/'
if not os.path.exists(pic_dir):
    os.mkdir(pic_dir)
for pic_url in resutle:
    pic_name = os.path.join(pic_dir, pic_url.split('/')[-1])
    try:
        get_web(pic_url, pic_name)
    except:
        pass
