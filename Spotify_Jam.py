import pyautogui
import time

# Give yourself a few seconds to switch to the desktop
for x in range(0, 1):
    pyautogui.hotkey("command", "space")
    time.sleep(2)

# Open Spotify (assuming it's pinned to the taskbar or you can use a keyboard shortcut)
pyautogui.hotkey("command", "space")
time.sleep(1)
pyautogui.write('Spotify.app')  
time.sleep(1)
pyautogui.press('enter')

# Wait for Spotify to open
time.sleep(5)

# Maximize the Spotify window
pyautogui.hotkey('control','command', 'f')

#Locating the queue option on spotify
location = pyautogui.locateOnScreen('Spotify-Queue.png')
pyautogui.click(location)

