import pyautogui
import time

# Give yourself a few seconds to switch to the desktop
for x in range(0, 1):
    pyautogui.hotkey("command", "space")
    time.sleep(1.5)

# Open Spotify (assuming it's pinned to the taskbar or you can use a keyboard shortcut)
pyautogui.hotkey("command", "space")
time.sleep(0.5)
pyautogui.write('Spotify.app')  
time.sleep(0.5)
pyautogui.press('enter')

# Wait for Spotify to open
time.sleep(5)

# Maximize the Spotify window
pyautogui.hotkey('control','command', 'f')

#Locating the connect to device option on spotify
location = pyautogui.click (1250,912)
time.sleep(1)

#Locating the create a jam option on spotify
location = pyautogui.click (1267,278)
time.sleep(1)

# Locating the create a jam option on spotify
# location = pyautogui.click (1312,407)
# time.sleep(1.2) 

# Open Whatsapp in full screen
pyautogui.hotkey("command", "space")
time.sleep(1)
pyautogui.write('whatsapp')  
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('fn', 'f')
time.sleep(1)

# Click on the chat boxCLICK ON SEARCH BUTTON
location = pyautogui.click(204,107)
time.sleep(0.5)

# Search Jainam Shah
pyautogui.write('Jainam Shah')
time.sleep(0.5)

# Click on first option
location = pyautogui.click(224,215)
time.sleep(0.5)

# Click on Searchbar
location = pyautogui.click(653,932)
time.sleep(0.5)

# Paste the code
pyautogui.hotkey("command", "v")
time.sleep(0.5)

# Click Enter
pyautogui.hotkey("return")
time.sleep(0.5)
