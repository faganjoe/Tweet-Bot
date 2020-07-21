from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username=input('username ')
password=input('password')
tweet=input("tweet")

PATH='/Users/joelfagan/Documents/Python Projects/chromedriver'
driver=webdriver.Chrome(PATH)


time.sleep(5)
driver.get('https://twitter.com/login')





try:
    user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session[username_or_email]"))
    )
    keyword = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session[password]"))
    )
    user.send_keys(username)
    keyword.send_keys(password)
    keyword.send_keys(Keys.ENTER)

except:
    driver.quit()

time.sleep(10)

find_tweet=driver.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div''')
find_tweet.send_keys(tweet)
send_tweet=driver.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/span/span''')
send_tweet.click()
