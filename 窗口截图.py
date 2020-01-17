import win32gui, win32ui, win32con
from ctypes import windll
from PIL import Image
import cv2
import numpy
import sys

显示比例 = 1.25
#获取后台窗口的句柄，注意后台窗口不能最小化
try:
    hWnd = win32gui.FindWindow("WeChatMainWndForPC",None) #窗口的类名可以用Visual Studio的SPY++工具获取
#获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
except Exception as e:
    print(e)
    exit(-1)
width = int((right - left) * 显示比例)
height = int((bot - top) * 显示比例)
#返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
hWndDC = win32gui.GetWindowDC(hWnd)
#创建设备描述表
mfcDC = win32ui.CreateDCFromHandle(hWndDC)
#创建内存设备描述表
saveDC = mfcDC.CreateCompatibleDC()
#创建位图对象准备保存图片
saveBitMap = win32ui.CreateBitmap()
#为bitmap开辟存储空间
saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
#将截图保存到saveBitMap中
saveDC.SelectObject(saveBitMap)
#保存bitmap到内存设备描述表
saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)

saveBitMap.SaveBitmapFile(saveDC,sys.path[0]  + "/Wechat.bmp")

win32gui.DeleteObject(saveBitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hWnd,hWndDC)

print('截图成功')