# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)

print("====== Game Start=======")

# output tab title
print(driver.title)

#  =======  init start ====== 

# bet count
betingCount = 86400

# bet amount
betAmount = 2

# bet number xpath
betNumberXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[7]/div[1]'; 
# bet multi xpath
betMultiXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[7]/div[2]'
# bet button xpath
betBtnXpath = '//*[@id="crash-control-0"]/div[2]/div/button'
# bet button text xpath
betBtnTxtXpath = '//*[@id="crash-control-0"]/div[2]/div/button/div/div'
# bet button text xpath
betBtnSubTxtXpath = '//*[@id="crash-control-0"]/div[2]/div/button/div/div[2]'
# bet button text xpath
betAutoMultiXpath = '//*[@id="crash-control-0"]/div[2]/div/div/div[2]/div[2]/input'

# bet number
betNumber = driver.find_element(By.XPATH, betNumberXpath).text
# bet multi
betMulti = driver.find_element(By.XPATH, betMultiXpath).text
print("betNumber ==" + betNumber + "==")
print("betMulti " + betMulti)
# bet Button
betBtn = driver.find_element(By.XPATH, betBtnXpath)
# bet cash out
betAutoMulti = driver.find_element(By.XPATH, betAutoMultiXpath) 
# bet start check
betStart = False
totalCount = 0


for x in range(betingCount):
    # wait 1 seconds
    time.sleep(0.5)  
    try :
        betBtnSubTxtData = driver.find_element(By.XPATH, betBtnSubTxtXpath).text
        betStart = False
    except :
        if(betStart == False): 
            time.sleep(0.5)      
            strBetMulti = str(driver.find_element(By.XPATH, betMultiXpath).text).replace("x", "")            
            if(strBetMulti != "" ):
                betMulti = float(strBetMulti)
                if(betMulti >= 5):
                    totalCount += 1
                    print("New Game start")
                    print("count is " + str(totalCount))
                    print("betMulti ====" + strBetMulti + "==========") 
                    betBtn = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, betBtnXpath)))                  
                    for y in range(20):
                            betAutoMulti.send_keys(Keys.BACKSPACE)
                    betAutoMulti.send_keys(str(betAmount))
                    betBtn.click()
                    betStart = True
        pass    
print("====== Game End=======")
time.sleep(1000)
driver.close()
driver.quit()