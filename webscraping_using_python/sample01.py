from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://realpython.com/python-web-scraping-practical-introduction/")
print(driver.current_url)

WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".article-body .toc li")))
toc = driver.find_elements_by_css_selector(".article-body .toc li")
for el in toc:
    print(el.text)

driver.close()
driver.quit()