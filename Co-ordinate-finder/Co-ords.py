import pyautogui
import time

# Get the current mouse position
while True:
    x, y = pyautogui.position()
    print("Mouse position:", x, y)
    time.sleep(1.5)