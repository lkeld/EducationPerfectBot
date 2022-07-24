from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import colorama
from colorama import Fore
import time
import sys
import json


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)


driver = webdriver.Chrome()
driver.get("https://app.educationperfect.com/app/login") 
try:
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, "//*[@id="login-username"]")) #This is a dummy element
)
print(FORE.green + 'Successfully Loaded Education Perfect')

time.wait(0.1)

print(FORE.green + 'Logging In')
.... sys.stdout.write(".")
.... sys.stdout.flush()
.... time.sleep(.1)
....
...........>>>

driver.find_element(By.XPATH, '//*[@id="login-username"]')
element.send_keys("eldril1@rokstu.catholic.edu.au")

time.wait(0.01)

driver.find_element(By.XPATH, '//*[@id="login-password"]')
element.send_keys("Lpasta22")

print(FORE.green + 'Successfully Logged In')
.... sys.stdout.write(".")
.... sys.stdout.flush()
.... time.sleep(.1)
....
...........>>>

elem = WebDriverWait(driver, 30).until(
    EC.prescence_of_element_located((By.XPATH, "//*[@id="nav-score"]/span[2]/span"))
)

driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div[9]/div')
element.click()
