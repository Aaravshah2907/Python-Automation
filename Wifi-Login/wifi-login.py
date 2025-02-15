from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the Chrome driver
service = webdriver.ChromeService() # Update with the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

def login():
    try:
        # Open the website
        driver.get('http://192.168.1.1/')  # Replace with the URL of the website you want to open

        # Wait for the form to be present
        time.sleep(2)
        
        # Read username and password from a file
        with open('wifi-credentials.json') as f:  # Update with the path to your credentials file
            credentials = json.load(f)
            username = credentials['username']
            password = credentials['password']

        # Fill out the form fields with the credentials
        username_field = driver.find_element(By.XPATH, '//*[@id="ft_un"]')  # Replace with the actual XPATH of the username field
        username_field.send_keys(username)  # Use the username from the file
        time.sleep(0.5)

        password_field = driver.find_element(By.XPATH, '//*[@id="ft_pd"]')  # Replace with the actual XPATH of the password field
        password_field.send_keys(password)  # Use the password from the file
        time.sleep(0.1)

        # Submit the form
        submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/form/div[3]/button')  # Replace with the actual XPATH of the submit button
        submit_button.click()

        # Wait for some time to see the result
        time.sleep(2.5)

    finally:
        # Close the browser
        driver.quit()


login()