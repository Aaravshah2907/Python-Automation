from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service   
from webdriver_manager.chrome import ChromeDriverManager

#create chromeoptions instance
options = webdriver.ChromeOptions()
options. add_argument("user-data-dir=/Users/aaravshah2975/Library/Application Support/Google/Chrome/")
options.add_experimental_option("detach", True)

#specify where your chrome driver present in your pc
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

#provide website url here
driver.get("https://www.linkedin.com/feed/")
print("Opened Linkedin")

#find element using its id

# Open via xpath

#print(driver.find_element("id","home").text)