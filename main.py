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
import os



print("""

▓█████  ██▓███      ▄▄▄       ██▓ ▒█████  
▓█   ▀ ▓██░  ██▒   ▒████▄    ▓██▒▒██▒  ██▒
▒███   ▓██░ ██▓▒   ▒██  ▀█▄  ▒██▒▒██░  ██▒
▒▓█  ▄ ▒██▄█▓▒ ▒   ░██▄▄▄▄██ ░██░▒██   ██░
░▒████▒▒██▒ ░  ░    ▓█   ▓██▒░██░░ ████▓▒░
░░ ▒░ ░▒▓▒░ ░  ░    ▒▒   ▓▒█░░▓  ░ ▒░▒░▒░ 
 ░ ░  ░░▒ ░          ▒   ▒▒ ░ ▒ ░  ░ ▒ ▒░ 
   ░   ░░            ░   ▒    ▒ ░░ ░ ░ ▒  
   ░  ░                  ░  ░ ░      ░ ░  
                                          """)
                                          
time.sleep(0.5)
print("Created With ❤ By lk#9999 | t.me/lkeld")
time.sleep(0.5)


menu = {}
menu['1']="Start EP AIO" 
menu['2']="Exit"
  options=menu.keys()
  options.sort()
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("Please Select:") 
    if selection =='1': 
        continue,
    elif selection == '2': 
      sys.exit(0)
      break
    else: 
      print "Unknown Option Selected!" 

# Check If AIO Is Latest Version
def check_up_to_date():
    url = "https://lukedev.me/edperfect.html"
    response = requests.get(url)
    data = response.text
    if Version in data:
        print(Fore.LIGHTGREEN_EX + "AIO Up To Date :)")
    else:
        print(Fore.RED + "Education Perfect AIO Is out of date\nLink: ")
    return


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)


driver = webdriver.Chrome()
driver.get("https://app.educationperfect.com/app/login") 
try:
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, "//*[@id="login-username"]")) 
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
time.sleep(0.5)
print(FORE.green + 'Loading Menu')
.... sys.stdout.write(".")
.... sys.stdout.flush()
.... time.sleep(.1)
....
...........>>>

menu = {}
menu['1']="English Lists" 
menu['2']="Japanese Lists"
menu['3']="Australian Languages Lists"
menu['4']="French Lists"
menu['5']="Exit"
while True: 
  options=menu.keys()
  options.sort()
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("Please Select:") 
    if selection =='1': 
      # put in action here
    elif selection == '2': 
      # put in action here
    elif selection == '3':
      # put in action here 
    elif selection == '4': 

    elif selection == '5':
        sys.exit(0)
        
      break
    else: 
      print "Invalid Option Selection",
      os.system('python main.py')


    
