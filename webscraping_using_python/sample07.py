from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://macro.test-webmaster.com/")
driver.maximize_window()
time.sleep(300)
driver.close()