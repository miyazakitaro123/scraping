# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as EXCEPT1
from selenium.common.exceptions import StaleElementReferenceException as EXCEPT2
import requests
import json


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)

print("====== Start =======")

# output tab title
# print(driver.title)

#  =======  init start ====== 

# bet count
bettingTotalCount = 10000

# bet amount
# betAmount = [0.001, 0.002, 0.004, 0.008, 0.016]
betAmount = [0.001, 0.002, 0.004, 0.008, 0.016, 0.032, 0.064, 0.128]
# betAmount = [0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28]
# betAmount = [1, 2, 4, 8, 16, 32, 64, 128]

# bet Amount Multi
betAmountMulti = 30

# bet multi amount
betMultiAmount = 4

# bet number xpath
betNumberXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[4]/div[1]'; 
# bet multi xpath
betMultiXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[4]/div[2]'
# bet button xpath
betBtnXpath = '//*[@id="crash-control-0"]/div[2]/div/button'
# bet button text xpath
betBtnTxtXpath = '//*[@id="crash-control-0"]/div[2]/div/button/div/div'
# bet button Sub text xpath
betBtnSubTxtXpath = '//*[@id="crash-control-0"]/div[2]/div/button/div/div[2]'
# bet auto multi xpath
betAutoMultiXpath = '//*[@id="crash-control-0"]/div[2]/div/div/div[2]/div[2]/input'
# bet auto amount xpath
betAutoAmountXpath = '//*[@id="crash-control-0"]/div[2]/div/div/div[1]/div[2]/input'


# bet amount
betAutoAmount = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, betAutoAmountXpath)))
# bet cash out
betAutoMulti = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, betAutoMultiXpath)))

# bet start check
betStart = False
#All Betting Multi
allBet = [{'mumber': 200, 'multi': 2.2}]
# Count Betting
bettingCount = 0
lastBetNumber = 0
# Max cross count
MaxCount = 1
#temp bet list
tempBetList = []
# same as game bet List 
gameBetList = [[1,1], [3,3], [1,1], [3,3]]
# total Win Count
totalWinCount = 0
# last ten count
lastTenCount = 0

def show_the_day(count, order, amount):
        URL = "https://shop.test-webmaster.com/api/bettings/add"
        # URL = "http://localhost:8000/api/bettings/add"
        PARAMS = {'count':count, 'order':order , 'amount': amount}
        requests.get(url = URL, params = PARAMS) 
        # pretty = json.dumps(response.json(), indent=2)
        # res = open('result.json', mode='w')
        # res.write(pretty)

while bettingCount < bettingTotalCount:
    betNumber = 0    

    try :
        betBtnSubTxtData = driver.find_element(By.XPATH, betBtnSubTxtXpath).text
        betStart = False
    except (EXCEPT1, EXCEPT2) :
                
        if(betStart == False):                      
            strBetMulti = str(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, betMultiXpath))).text).replace("x", "")

            if(strBetMulti != "" ):
                betMulti = float(strBetMulti)
                # bet number
                betNumber = int(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, betNumberXpath))).text)
                multiPair = {'mumber': betNumber, 'multi': betMulti}
                if(betNumber != allBet[-1]['mumber']):
                    betStart = True
                    lastTenCount += 1
                    print("lastTenCount", str(lastTenCount))
                    allBet.append(multiPair)

                    # temp validate
                    if(not((len(tempBetList) == 0) or (tempBetList[-1] > 2 and betMulti > 2) or (tempBetList[-1] <= 2 and betMulti <= 2))):
                        gameBetList.append(tempBetList)
                        tempBetList = []                        
                    tempBetList.append(betMulti)

                    if(betMulti >= 10):  
                        print("call function")
                        show_the_day(lastTenCount, betNumber, betMulti) 
                        lastTenCount = 0                                  
                        bettingCount += 1
                        # Start bet
        pass    
print("====== End=======")



driver.close()
driver.quit()