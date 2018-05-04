from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe')

driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

# maximize the window size
driver.maximize_window()

# find element by xpath 
email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('XXXX@gamil.com') # insert gmail address

time.sleep(3)

# find element by xpath 
password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('XXXXX') # insert linked in password

time.sleep(3)

# find element by xpath 
login = driver.find_element_by_xpath('//*[@id="btn-primary"]')
login.click()

time.sleep(5)

#close the drive
driver.quit()
