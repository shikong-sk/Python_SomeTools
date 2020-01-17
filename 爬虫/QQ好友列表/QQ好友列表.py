from selenium import webdriver
import time,re
print('输入QQ账号：',end='')
username = str(input()) #QQ账号
print('输入登录密码：',end='')
password = str(input()) #QQ密码
print('代码执行中，请稍后')
opt = webdriver.FirefoxOptions()# 调用火狐
opt.add_argument('--headless')#后台启动火狐
browser = webdriver.Firefox(options=opt,executable_path="C:\爬虫驱动\geckodriver.exe")# 加载驱动 && 创建Firefox无界面对象
# browser = webdriver.Chrome(executable_path="C:\爬虫驱动\chromedriver.exe")#谷歌浏览器
browser.implicitly_wait(2)
browser.get('https://qzone.qq.com/')
browser.switch_to.frame('login_frame')
browser.find_element_by_css_selector("#switcher_plogin").click()
browser.find_element_by_css_selector("#u").send_keys(username)
browser.find_element_by_css_selector("#p").send_keys(password)
browser.find_element_by_css_selector("#login_button").click()
cookies={}

time.sleep(3)

browser.get_cookies()
print(len(browser.get_cookies()))
for i in browser.get_cookies():
    cookies[i.get('name')]=i.get('value')
print(cookies)
browser.switch_to.frame(None)
qzonetoken = re.findall(r'window.g_qzonetoken = \(function\(\){ try{return "(.*?)";}',browser.page_source)
print('qzonetoken:',qzonetoken)

import js2py
try:
    if(qzonetoken == []):
        exit(0)
    js_string = '''
    function(e) {
            var t = 5381;
            for (var n = 0, r = e.length; n < r; ++n) {
                t += (t << 5) + e.charCodeAt(n)
            }
            return t & 2147483647
        }
    '''
    js_function = js2py.eval_js(js_string)
    g_tk=js_function(cookies.get('p_skey'))
    print(g_tk)

    import requests

    url = "https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi"

    querystring = {
        "uin":cookies.get('ptui_loginuin'),
        "do":"1",
        "rd":"0.09717650107426145",
        "fupdate":"1",
        "clean":"1",
        "g_tk":[g_tk,g_tk],
        "qzonetoken":qzonetoken
    }

    headers = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'referer': "https://user.qzone.qq.com/%s"%cookies.get('ptui_loginuin'),
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }

    response = requests.request("GET", url, headers=headers, params=querystring,cookies=cookies)
    import re,json
    json_str = re.findall(r'\{.*\}',response.text,re.S)[0]
    obj = json.loads(json_str)
    for i in obj.get('data').get('items_list'):
        print(i.get('uin'),i.get('name'))
except:
    print('登录失败')
browser.quit()

print('程序执行完毕',end='')
import os
os.system('pause')