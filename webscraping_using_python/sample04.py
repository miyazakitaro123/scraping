
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.options import Options    

chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_argument("--start-fullscreen");
chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe",
                          chrome_options=chrome_options)

driver.get("https://macro.test-webmaster.com/")
driver.maximize_window()

# email=driver.find_element(by=By.XPATH, value="//*[@id='login']/div[1]/div[1]/div[2]/input")
# email.send_keys("typing")
# print(email)
time.sleep(300)
driver.close()