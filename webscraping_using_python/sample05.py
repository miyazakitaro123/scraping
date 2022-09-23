
# import module
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Lion\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 13")
driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe', options=options)
  
# get https://www.geeksforgeeks.org/
driver.get("https://www.geeksforgeeks.org/")
  
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(3)
  
# Obtain button by link text and click.
button = driver.find_element_by_link_text("Sign In")
button.click()