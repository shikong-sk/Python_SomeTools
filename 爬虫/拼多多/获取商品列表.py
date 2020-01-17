from selenium import webdriver
import time
import re
import os
import sys

URL = "https://apiv2.pinduoduo.com/api/gindex/subject/limited/goods?subject_id=%s&page=1&size=50"
target = ['5571', '5574', '22498', '5576', '5572', '5578']

opt = webdriver.FirefoxOptions()  # 调用火狐
# opt.add_argument('--headless')#后台启动火狐

print(os.path.join(sys.path[0], "驱动/geckodriver.exe"))

browser = webdriver.Firefox(options=opt, executable_path=os.path.join(
    sys.path[0], "驱动/geckodriver.exe"))  # 加载驱动 && 创建Firefox无界面对象
# browser = webdriver.Chrome(executable_path="C:\爬虫驱动\chromedriver.exe")#谷歌浏览器

browser.implicitly_wait(2)

for t in target:

    browser.get(URL.replace('%s', str(t)))

    jsonData = browser.find_element_by_css_selector("#json").text

    with open(os.path.join(sys.path[0], str(t)+'.json'), 'w+',encoding='utf-8') as f:
            f.write(jsonData.encode('utf-8').decode('utf-8'))
    print(jsonData.encode('utf-8').decode('utf-8'))

browser.quit()
