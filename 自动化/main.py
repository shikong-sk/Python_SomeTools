import os
import sys
import time
import platform


def window_capture(filename, scale=1):
    # hwnd = win32gui.FindWindow(None, "微信")

    # 获取后台窗口的句柄，注意后台窗口不能最小化
    try:
        hWnd = win32gui.FindWindow("WeChatMainWndForPC", '微信')  # 窗口的类名可以用Visual Studio的SPY++工具获取
        # 获取句柄窗口的大小信息
        # hwnd = win32gui.FindWindow(None, "地下城与勇士")
        left, top, right, bot = win32gui.GetWindowRect(hWnd)
    except Exception as e:
        print(e)
        exit(-1)
    win32gui.SetForegroundWindow(hWnd)
    width = int((right - left) * scale)
    height = int((bot - top) * scale)
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    saveBitMap.SaveBitmapFile(saveDC, filename)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd, hWndDC)
    x1, y1, x2, y2 = left * scale, top * scale, right * scale, bot * scale
    print('(' + str(x1), str(y1) + ')', '(' + str(x2), str(y2) + ')')
    return width, height


def key_down(key):
    win32api.keybd_event(key, 0, 0, 0)


def key_up(key):
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)


def key_put(key):
    key_down(key)
    key_up(key)


def key_inputs(key_input):
    for x in key_input:
        if isinstance(x, str):
            for i in x.upper():
                key_put(keyCode[i])
        elif isinstance(x, list):
            for i in x:
                key_put(keyCode[i])
        elif isinstance(x, tuple):
            key_put(keyCode[x[0]])


def key_sticky(key_inputs):
    for key in key_inputs:
        key_down(keyCode[key])
    for key in key_inputs:
        key_up(keyCode[key])


if __name__ == '__main__':

    try:
        import win32api, win32con, win32gui, win32ui
    except ModuleNotFoundError as e:
        print('缺少 pypiwin32 模块，准备安装：')
        os.system('pip install pypiwin32')
        import win32api, win32con, win32gui

    try:
        import pytesseract
    except ModuleNotFoundError as e:
        print('缺少 pytesseract 模块，准备安装：')
        os.system('pip install pytesseract')
        import pytesseract

    from PIL import Image, ImageGrab

    try:
        import cv2
    except ModuleNotFoundError as e:
        print('缺少 cv2 模块，准备安装：')
        os.system('pip install cv2')
        import cv2

    import tkinter as tk
    from tkinter import ttk
    from sys import exit
    from os import popen

    try:
        from numpy import load, save
        import numpy as np
    except ModuleNotFoundError as e:
        print('缺少 numpy 模块，准备安装：')
        os.system('pip install numpy')
        import numpy

    try:
        import pypinyin
    except ModuleNotFoundError as e:
        print('缺少 pypinyin 模块，准备安装：')
        os.system('pip install pypinyin')
        import pypinyin

    keyCode = {
        "Backspace": 8,
        "Tab": 9,
        "回车": 13,
        "Shift": 16,
        "Ctrl": 17,
        "Alt": 18,
        "Pause": 19,
        "大写": 20,
        "Esc": 27,
        "空格": 32,
        "PgUp": 33,
        "PgDn": 34,
        "End": 35,
        "Home": 36,
        "左": 37,
        "上": 38,
        "右": 39,
        "下": 40,
        "Select": 41,
        "Print": 42,
        "Insert": 45,
        "Delete": 46,
        "Help": 47,
        "0": 48,
        "1": 49,
        "2": 50,
        "3": 51,
        "4": 52,
        "5": 53,
        "6": 54,
        "7": 55,
        "8": 56,
        "9": 57,
        "=": 61,
        "A": 65,
        "B": 66,
        "C": 67,
        "D": 68,
        "E": 69,
        "F": 70,
        "G": 71,
        "H": 72,
        "I": 73,
        "J": 74,
        "K": 75,
        "L": 76,
        "M": 77,
        "N": 78,
        "O": 79,
        "P": 80,
        "Q": 81,
        "R": 82,
        "S": 83,
        "T": 84,
        "U": 85,
        "V": 86,
        "W": 87,
        "X": 88,
        "Y": 89,
        "Z": 90,
        "Win": 91,
        "Menu": 93,
        "_0": 96,
        "_1": 97,
        "_2": 98,
        "_3": 99,
        "_4": 100,
        "_5": 101,
        "_6": 102,
        "_7": 103,
        "_8": 104,
        "_9": 105,
        "*": 106,
        "+": 107,
        "-": 109,
        ".": 110,
        "/": 111,
        "F1": 112,
        "F2": 113,
        "F3": 114,
        "F4": 115,
        "F5": 116,
        "F6": 117,
        "F7": 118,
        "F8": 119,
        "F9": 120,
        "F10": 121,
        "F11": 122,
        "F12": 123,
        "小键盘": 144,
        "Scroll Lock": 145,
        "-": 173,
        "=": 187,
        ",": 188,
        "-": 189,
        ".": 190,
        "/": 191,
        "`": 192,
        "[": 219,
        "|": 220,
        "]": 221,
        "'": 222,
    }

    if 'Windows-10' in platform.platform():
        scale = 1.25
    else:
        scale = 1

    key_input = []
    # key_input = pypinyin.lazy_pinyin('时空旅行者')
    # print(key_input)
    time.sleep(2)

    # keys = ['Win', 'R']
    # key_input = [['Shift'], 'cmd', ['回车']]
    # print(type(key_inputs))
    # key_sticky(keys)
    # time.sleep(0.1)
    # key_inputs(key_input)
    # time.sleep(0.2)
    # key_inputs([['Shift'], 'systeminfo', ['回车']])

    # key_input.append(["1"])
    # key_input = keyCode.items()
    # for x in key_input:
    #     print(x[0])

    # key_inputs(key_input)
    for i in range(100):
        x, y = window_capture(os.path.join(sys.path[0], 'wx.jpg'), scale)
        print(x, y)
        time.sleep(0.1)

    window_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴

    window_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴
    print(window_width * scale, window_height * scale)
