import pyautogui
import time
mess = 3
while mess>0:
    time.sleep(4)
    pyautogui.typewrite('Call me')
    time.sleep(4)
    pyautogui.press('enter')
    mess = mess-1
