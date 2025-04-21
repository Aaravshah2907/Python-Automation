import subprocess

def get_wifi_ssid():
    # The command to get the SSID
    cmd = "ipconfig getsummary en0 | awk -F ' SSID : ' '/ SSID : / {print $2}'"
    # Run the command in the shell and capture output
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    ssid = result.stdout.strip()
    if ssid:
        print(f"Connected Wi-Fi SSID: {ssid}")
    else:
        print("Not connected to a Wi-Fi network or SSID could not be determined.")

if __name__ == "__main__":
    get_wifi_ssid()
