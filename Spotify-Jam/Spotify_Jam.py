import pyautogui as pg
import time

# Give yourself a few seconds to switch to the desktop
for x in range(0, 1):
    pg.hotkey("command", "space")
    time.sleep(1.5)

# Open Spotify (assuming it's pinned to the taskbar or you can use a keyboard shortcut)
pg.hotkey("command", "space")
time.sleep(0.5)
pg.write('Spotify.app')  
time.sleep(0.5)
pg.press('enter')

# Wait for Spotify to open
time.sleep(5)

# Maximize the Spotify window
pg.hotkey('control','command', 'f')

# Start playing songs
pg.click(734,874)
time.sleep(0.5)


#Locating the connect to device option on spotify
pg.click (1250,912)
time.sleep(1)

#Locating the create a jam option on spotify
pg.click (1267,278)
time.sleep(1)

# Locating the create a jam option on spotify
# location = pyautogui.click (1312,407)
# time.sleep(1.2) 

# Open Whatsapp in full screen
pg.hotkey("command", "space")
time.sleep(1)
pg.write('whatsapp')  
time.sleep(1)
pg.press('enter')
time.sleep(3)
pg.hotkey('fn', 'f')
time.sleep(1)

# Click on the chat boxCLICK ON SEARCH BUTTON
pg.click(204,107)
time.sleep(0.5)

# Search Jainam Shah
pg.write('Jainam Shah')
time.sleep(0.5)

# Click on first option
pg.click(224,215)
time.sleep(0.5)

# Click on Searchbar
pg.click(653,932)
time.sleep(0.5)

# Paste the code
pg.hotkey("command", "v")
time.sleep(0.5)

# Click Enter
pg.hotkey("return")
time.sleep(0.5)

# Exit whatsapp
pg.hotkey("command", "q")
time.sleep(0.5)