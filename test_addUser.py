from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

FIRSTNAME= 'Hung'
LASTNAME = 'Hoang'
USERNAME = 'hung'
PASSWORD = '12345'


s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('http://127.0.0.1:5501/adduserpage.html')

sleep(2)
firstName_input = driver.find_element_by_id('first-name')
firstName_input.send_keys(FIRSTNAME)

lastName_input = driver.find_element_by_id('last-name')
lastName_input.send_keys(LASTNAME)

user_input = driver.find_element_by_id('user-name')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('password')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('add-user')
sleep(2)
login_button.click()

sleep(5)
driver.close()