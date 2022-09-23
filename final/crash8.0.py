# PYTHON Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as EXCEPT1
from selenium.common.exceptions import StaleElementReferenceException as EXCEPT2
import time
import json
import datetime


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
betAmountMulti = 0.1

# bet multi amount
betMultiAmount = 2

# bet number xpath
betNumberXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[7]/div[1]'; 
# bet multi xpath
betMultiXpath = '//*[@id="game-crash"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[7]/div[2]'
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
allBeforeBet = [{'mumber': 200, 'multi': 2.2}]
allBet = [{'mumber': 200, 'multi': 2.2}]
# Count Betting
bettingCount = 0
# you lose count
loseCount = 0
lastBetNumber = 0
# Max cross count
MaxCount = 1
#Real All multi
allDoneBet = []
# a lot lose count
lotLoseCount = 0


# temp flag
tempFlag = False

# Set multi amount        
for y in range(10):
    betAutoMulti.send_keys(Keys.BACKSPACE)
betAutoMulti.send_keys(str(betMultiAmount))


while bettingCount < bettingTotalCount:   
        
    lastNumber = allBeforeBet[len(allBeforeBet)-1]['mumber'] + 1
    lastMulti = allBeforeBet[len(allBeforeBet)-1]['multi']
    
    betNumber = 0
    strBetNumber = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, betNumberXpath))).text
    strBetMulti = str(WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, betMultiXpath))).text).replace("x", "") 

    if(strBetNumber != "" and strBetMulti != ""):
        betNumber = int(strBetNumber)

        if(lastNumber == betNumber and betNumber != lastBetNumber):
            betMulti = float(strBetMulti)
            multiPair = {'mumber': betNumber, 'multi': betMulti}
            # add betMulti
            allDoneBet.append(multiPair)
            lastBetNumber = lastNumber
            
            bettingCount += 1
            if(betMulti <= 2):
                loseCount += 1
                if(loseCount == 8):
                    loseCount = 0
                    lotLoseCount += 1
                    print(" Y l a l : " + str(lotLoseCount))
            else:
                loseCount = 0
                if(not((tempFlag == True) and ((allDoneBet[len(allDoneBet)-1]['mumber'] -  allDoneBet[len(allDoneBet)-2]['mumber']) == 1))):
                    tempFlag = not(tempFlag)

            now = datetime.datetime.now()
            print(" lBN: " + str(lastBetNumber) + "  lC: " + str(loseCount) + " tempFlag: " + str(tempFlag) + " Current date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") )


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
                allBet.append(multiPair)                
                beforeBetmulti =  allBet[len(allBet)-2]['multi']
                nearBeforeBetmulti =  allBet[len(allBet)-1]['multi']

                # bet triger flag
                trigerFlag = False                

                if(tempFlag):
                    trigerFlag = (betMulti > 2)
                else:
                    trigerFlag = (beforeBetmulti > 2 and betMulti < 2)
                    
                if(trigerFlag):          
                    # add betMulti
                    allBeforeBet.append(multiPair)    

                    # Set bet amount
                    for y in range(15):
                        betAutoAmount.send_keys(Keys.BACKSPACE)   

                    betAutoAmount.send_keys(str(betAmount[loseCount] * betAmountMulti)) 
                    # Click bet
                    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, betBtnXpath))).click()
                    # Start bet
                    betStart = True
        pass    
print("====== End=======")

# save multi data
multiDataFile = open("multidata.json", "w")
json.dump(allDoneBet, multiDataFile, indent = 6) 

driver.close()
driver.quit()