from selenium import webdriver
import os
import time
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



def login(username,password,user,msg,n):
    bot=driver
    bot.get('https://www.instagram.com/')
    enter_username = WebDriverWait(bot, 20).until(
		expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)
    enter_password = WebDriverWait(bot, 20).until(
		expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)
    time.sleep(10)

    #closing first popup
    bot.find_element_by_xpath(
		'//*[@class="cmbtv"]/button').click()
    time.sleep(2)

    
    #closing second popup
    bot.find_element_by_xpath(
		'//*[@class="mt3GC"]/button[2]').click()
    time.sleep(4)

    
    #clicking on direct button
    bot.find_element_by_xpath(
		'//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Messenger"]').click()
    time.sleep(3)
       
    
    #clicking on pencil button
    bot.find_element_by_xpath(
		'//*[@class="_2NzhO EQ1Mr"]/button').click()
    time.sleep(2)

    for r in range(n):
        for i in user:

            # enter the username
            bot.find_element_by_xpath(
                '//*[@class=" HeuYH"]/input').send_keys(i)
            time.sleep(4)
            
            # click on the username
            bot.find_element_by_xpath(
                '//*[@class="-qQT3"]').click()
            time.sleep(2)
            
            # next button
            bot.find_element_by_xpath(
                '//*[@class="WaOAr"][2]/div/button').click()
            time.sleep(2)
            
            # click on message area
            send = bot.find_element_by_xpath(
                '//*[@class="X3a-9"]/div[2]/textarea')
            
            # types message
            send.send_keys(msg)
            time.sleep(1)
            
            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)
            
            # clicks on direct option or pencil icon
            bot.find_element_by_xpath(
                '//*[@class="_2NzhO EQ1Mr"]/button').click()
            time.sleep(2)


username=str(input('Enter your Username: '))
password = getpass("Enter your password:  ")
user=list(map(str,input("Enter the usernames to msg separated with spaces: ").split()))
msg=str(input("Enter the msg to send: "))
n=int(input("Enter the number of times to send the message: "))
driver = webdriver.Chrome(ChromeDriverManager().install())
login(username,password,user,msg,n)
print("\nDone !")