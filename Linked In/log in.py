from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

driver.maximize_window()

email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('tomhankss500@gmail.com')

time.sleep(3)

password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('s-p*_GY.ECn\G8k:')

time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="btn-primary"]')
login.click()

time.sleep(5)

driver.quit()



