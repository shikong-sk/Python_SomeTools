import requests
import re
url = 'http://123.206.87.240:8002/qiumingshan/'
s = requests.Session()
source = s.get(url)
expression = re.search(r'(\d+[+\-*])+(\d+)', source.text).group()  #正则表达式，匹配算术计算
result = eval(expression)
post = {'value': result}
print(post)
print(s.post(url, data = post).text)