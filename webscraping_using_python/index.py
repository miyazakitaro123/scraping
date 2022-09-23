# PYTHON Example
from ast import For
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "C:\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)

print("======End Game Start=======")

# output tab title
print(driver.title)


# init result
betingCount = 10
result = 0
loseCount = 0
maxLose = 0
allResults = []
# BNB Coin
# betAmountList = [0.0001, 0.0002, 0.0003, 0.0004]
betAmountList = [0.0001, 0.001, 0.007, 0.04]
# Bet Coin
# betAmountList = [100, 500, 3000, 10000]
betAmount = betAmountList[0]
multiples = ['0.00x','1.20x','1.50x']


# amount
amount = driver.find_element(By.XPATH, '//*[@id="Wheel-control-0"]/div[2]/div/div[1]/div[2]/input') 
# Get Start My Account Amount
myWalletAmount_xpath = '//*[@id="header"]/div[2]/div[2]/div[1]/div/div/div[2]/div/span'
myWalletAmount = driver.find_element(By.XPATH, myWalletAmount_xpath).text    
print(" My Wallet Start Amount is " + str(myWalletAmount))

# start process
for x in range(betingCount):
    betAmount = betAmountList[loseCount]
    # empty betAmount Input
    for y in range(50):
        amount.send_keys(Keys.BACKSPACE)
    # enter betAmount
    amount.send_keys(str(betAmount))

    # click bet button
    betBtn = driver.find_element(By.XPATH, '//*[@id="Wheel-control-0"]/div[2]/div/button')
    betBtn.click() 

    # wait 7 seconds
    time.sleep(7)   

    # Get bet Result
    result = driver.find_element(By.XPATH, '//*[@id="game-Wheel"]/div[1]/div/div[2]/div[1]/div[2]/div/div[9]/div').text    
    # Print Out Result
    # print("result is"+result)
    # Push bet result into Array 
    allResults.append(result)
    # Calculate lose count
    if(result == multiples[0]) :
        maxLose += 1
        loseCount += 1
    else :
        maxLose = 0
        loseCount = 0

    if(loseCount == 4):
        loseCount = 0

# end process

myWalletAmount = driver.find_element(By.XPATH, myWalletAmount_xpath).text
print(" My Wallet End Amount is " + str(myWalletAmount))

print(" Betting Total Count is " + str(len(allResults)))
print(" Betting lose Count " + multiples[0] + " is " + str(allResults.count(multiples[0])))
print(" Betting win Count " + multiples[1] + " is " + str(allResults.count(multiples[1])))
print(" Betting win Count " + multiples[2] + " is " + str(allResults.count(multiples[2])))

print("======End Game Part=======")

print("======detail Information Part=======")
inforLostArray = []
inforLose = 0
for x in range(betingCount):
    if(allResults[x] == multiples[0]):
        inforLose += 1
    else :
        if(inforLose > 0):
            inforLostArray.append(inforLose)
        inforLose = 0
print(inforLostArray)
print("======detail Information Part=======")

driver.close()
driver.quit()