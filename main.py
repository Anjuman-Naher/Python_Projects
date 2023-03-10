import pyautogui
import time
message = 5
while message > 0:
    time.sleep(2)
    pyautogui.typewrite("Thanks for teach me something new")
    time.sleep(1)
    pyautogui.press("enter")
    message = message - 1