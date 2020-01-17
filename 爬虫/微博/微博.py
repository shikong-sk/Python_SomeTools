import json
import sys
from time import sleep

import requests


class API:
    serviceURL = "https://m.weibo.cn/api/"
    config = serviceURL + "config"
    channelList = serviceURL + "config/list"
    contain = serviceURL + "container/getIndex?containerid="
    lbs = serviceURL + "lbs/near?"
    detail = serviceURL + "detail/"
    hotflow = serviceURL + "../comments/hotflow?id=%s&mid=%s"


headers = {
    "Host": "m.weibo.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
}

cookies = {
    "M_WEIBOCN_PARAMS": "luicode=10000011&lfid=102803&uicode=10000011&fid=102803",
    "WEIBOCN_FROM":"1110006030"
}

def getXsrf_token():
    url = API.config
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("连接失败", e.args)

def getChannel():
    url = API.channelList
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("连接失败", e.args)


channel = getChannel()
channel = channel["data"]["channel"]

xsrf_token = getXsrf_token()["data"]["st"]

cookies['XSRF-TOKEN'] = xsrf_token

for x in channel:
    for k, y in x.items():
        print(k + ":" + y)
    print("-" * 50)


def getContain(gid, page):
    if gid == "lbs":
        url = API.lbs
        data = {"page": str(page)}
    else:
        url = API.contain
        # data = {"containerid": gid, "page": str(page)}
        # data = {"containerid": gid, "since_id": str(page)}
        data = {"containerid": gid, "page": str(page), "since_id": str(page)}

    try:
        response = requests.get(url, headers=headers, params=data,cookies=cookies)
        print(response.headers)
        try:
            assert response.status_code == 200,'IP被微博拉入黑名单，请稍后再试'
            return response.json()
        except e:
            sys.exit(-1)
        # if response.status_code == 200:
            # return response.json()
        # else:
        #     print(response.status_code)
            # assert()
    except requests.ConnectionError as e:
        print("连接失败", e.args)
    
    xsrf_token = getXsrf_token()["data"]["st"]

    cookies['XSRF-TOKEN'] = xsrf_token


message = []

for page in range(1, 50 + 1):
    print("-" * 20 + "page:" + str(page) + "-" * 20)
    datas = getContain(channel[0]["gid"], page)

    for data in datas["data"]["cards"]:
        if data["mblog"]["mid"] in message:
            print(data["mblog"]["mid"], "已存在")
        elif data in message:
            print(data["mblog"]["mid"], "已存在")
        else:
            message.append(data["mblog"]["mid"])
            print(data["mblog"]["mid"])


    if page % 10 == 0:
        sleep(2)

print("累计请求", page, "页,共", len(message), "条有效数据")
