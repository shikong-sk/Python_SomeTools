import pyautogui
import time
for x,y in pyautogui.__dict__.items():
    print(str(x) + '\t:\t' + str(y))