# PYTHON Example
import math
from tkinter import FALSE
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as EXCEPT1
from selenium.common.exceptions import StaleElementReferenceException as EXCEPT2
from datetime import datetime




chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)

print("====== Game Start =======")

# output tab title
# print(driver.title)

#  =======  init start ====== 

# bet count
bettingTotalCount = 10000

# bet number xpath
betNumberXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[4]/div[1]'; 
# bet multi xpath
betMultiXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[4]/div[2]'
# Red bet button xpath
RedBetBtnXpath = '//*[@id="crash-control-0"]/div[2]/div/div[2]/button'
# Green bet button xpath
GreenBetBtnXpath = '//*[@id="crash-control-0"]/div[2]/div/div[3]/button'
# Moon bet button xpath
MoonBetBtnXpath = '//*[@id="crash-control-0"]/div[2]/div/div[4]/button'
# Moon bet button Sub text xpath
betBtnSubTxtXpath = '//*[@id="crash-control-0"]/div[2]/div/div[4]/button/div/div[2]'
# bet auto amount xpath
betAutoAmountXpath = '//*[@id="crash-control-0"]/div[2]/div/div[1]/div[2]/input'
# current amount xpath
currentAmountXpath = '//*[@id="header"]/div[2]/div[2]/div[1]/div/div/div[2]/div/span'

# bet amount
betAutoAmount = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, betAutoAmountXpath)))

# bet start check
betStart = False
#All Betting Multi
allBet = [{'mumber': 200, 'multi': 2.2}]
# Count Betting
bettingCount = 0
#temp bet list
tempBetList = []
# same as game bet List 
gameBetList = [[1,1], [3,3], [1,1], [3,3], [1,1], [3,3]]

# max betting amount 
maxBettingCount = 4

# start betting amount 
standardBettingAmount = 0.2

# last betting amount 
loseCount = 0

# betting amount
bettingAmount = 0

# betting button type
bettingType = FALSE

# betting start hour
start_hour = 21

# betting end hour
end_hour = 4

# betting morning start hour
morning_start_hour = 8

# betting morning end hour
morning_end_hour = 9

startCurrentAmount =  float(str(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, currentAmountXpath))).text).replace("$", ""))

print("Game Started")
print("startCurrentAmount" + str(startCurrentAmount))


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

                now = datetime.now()
                current_hour = now.hour

                if(betNumber != allBet[-1]['mumber']):

                    currentAmount =  float(str(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, currentAmountXpath))).text).replace("$", ""))
                    # day target verify
                    if(currentAmount > startCurrentAmount + standardBettingAmount * 50):
                        break

                    betStart = True
                    allBet.append(multiPair)

                    # temp validate
                    if(not((len(tempBetList) == 0) or (tempBetList[-1] > 2 and betMulti > 2) or (tempBetList[-1] <= 2 and betMulti <= 2))):
                        gameBetList.append(tempBetList)
                        tempBetList = []
                    tempBetList.append(betMulti)                    

                    if((tempBetList[-1] < 2 and bettingType) or (tempBetList[-1] > 2 and not(bettingType))):                        
                        loseCount = loseCount + 1
                        if(loseCount == maxBettingCount):
                            loseCount = 0
                    else :
                        loseCount = 0
                        
                    # calculate betting amount
                    if(loseCount > 0):
                        bettingAmount = standardBettingAmount * math.pow(2, loseCount)
                    else:
                        bettingAmount = standardBettingAmount

                    print("bettingAmount" + str(bettingAmount))
                    
                    # Set bet amount
                    for y in range(15):
                        betAutoAmount.send_keys(Keys.BACKSPACE)
                    betAutoAmount.send_keys(str(bettingAmount))    

                    # Click bet Button
                    if((len(tempBetList) == 1 and len(gameBetList[-1]) == 1 and len(gameBetList[-2]) == 1) or (len(tempBetList) == 2 and len(gameBetList[-1]) == 1 and len(gameBetList[-2]) == 1 and len(gameBetList[-3]) == 1)):
                        if(betMulti < 2):
                            bettingType = True
                            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, GreenBetBtnXpath))).click()                        
                        else:
                            bettingType = False
                            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, RedBetBtnXpath))).click()
                    else:
                        if(betMulti < 2):
                            bettingType = False
                            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, RedBetBtnXpath))).click()
                        else:
                            bettingType = True
                            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, GreenBetBtnXpath))).click()

        pass    
print("====== Game End =======")

driver.close()
driver.quit()