import pyautogui as pg
import time
import json

# Give yourself a few seconds to switch to the desktop
for x in range(0, 1):
    pg.hotkey("command")
    print(f"{x} seconds.....")

# Open Spotify (use a keyboard shortcut)
pg.hotkey("command", "space")
time.sleep(0.5)
pg.write('Spotify.app')  
time.sleep(0.5)
pg.press('enter')

# Wait for Spotify to open
time.sleep(4)

# Maximize the Spotify window
pg.hotkey('control','command', 'f')
time.sleep(1)

# Start playing songs
pg.click(735,894)
time.sleep(0.5)

#Locating the connect to device option on spotify
pg.click (1381,64)
time.sleep(1)

#Locating the create a jam option on spotify
pg.click (1136,252)
time.sleep(1)

with open('credentials.json') as f:  # Update with the path to your credentials file
    credentials = json.load(f)
    shareto = credentials['shareto']
    
# Open Whatsapp in full screen
pg.hotkey("command", "space")
time.sleep(1)
pg.write('whatsapp')  
time.sleep(1)
pg.press('enter')
time.sleep(5)
pg.hotkey('fn', 'f')
time.sleep(1.5)

# Click on the chat boxCLICK ON SEARCH BUTTON
pg.hotkey('command', 'n')
time.sleep(0.5)
pg.hotkey('tab')

# Search Name imported from the json file
pg.write(shareto)
time.sleep(1.5)

# Click on first option
pg.click(328,220)
time.sleep(1)

# Paste the code
pg.hotkey("command", "v")
time.sleep(0.5)

# Click Enter
pg.hotkey("return")
time.sleep(1)

# Exit whatsapp
pg.hotkey("command", "q")
time.sleep(0.5)