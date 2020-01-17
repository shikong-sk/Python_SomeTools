import pyautogui
import time
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1
W,H = pyautogui.size()
print('屏幕分辨率：' + str(W) + 'x' + str(H))
x = y = 0
while 1:
    if ((x,y) != pyautogui.position()):
        x,y = pyautogui.position()
        print(x,y)
    time.sleep(0.1)
        # txt = str(x)+str(y)
        # pyautogui.alert(text=txt, title='Test')