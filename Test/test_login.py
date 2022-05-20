from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

brower = webdriver.Chrome(ChromeDriverManager().install())
#brower = webdriver.Chrome(executable_path="chromedriver.exe")
# open link facebook.com, change url for expect url
brower.get("http://127.0.0.1:5500/testrepo/Test/login.html")
sleep(2)
# get id html username input
txt_user = brower.find_element(By.ID, "username")
#get id password
txt_password = brower.find_element(By.ID, "login")
#set username and password in website
txt_user.send_keys('testuser')
txt_password.send_keys('12345')
txt_password.send_keys(Keys.ENTER)

sleep(10)
brower.close()