
# import module
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
  
# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.
options = Options()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.headless = True
driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe", options=options)
  
# get https://www.geeksforgeeks.org/
driver.get("https://bc.game")

driver.save_screenshot('screenshot.png')
  
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
time.sleep(1000)
  
# Obtain button by link text and click.
# button = driver.find_element_by_link_text("Sign In")
# button.click()