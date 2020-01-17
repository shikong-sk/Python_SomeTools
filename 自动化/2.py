import pyautogui
import time
# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.1
W,H = pyautogui.size()
print('屏幕分辨率：' + str(W) + 'x' + str(H))
# x = y = 0
# while 1:
#     if ((x,y) != pyautogui.position()):
#         x,y = pyautogui.position()
#         print(x,y)
#     time.sleep(0.1)
#         # txt = str(x)+str(y)
#         # pyautogui.alert(text=txt, title='Test')

def draw(location,time):
    while location > 0 :
        pyautogui.dragRel(location,0,time,button='left')
        location -= 10
        pyautogui.dragRel(0,location,time,button='left')
        pyautogui.dragRel(-location,0,time,button='left')
        location -= 10
        pyautogui.dragRel(0,-location,time,button='left')

time = 0
for location in range(200,400,25):
    pyautogui.moveTo(location,location)
    draw(location,time)