# a class="result-image"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def login_and_search():	

	driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

	driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

	driver.maximize_window()

	email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
	email.send_keys('xxxxx@gmail.com') # insert email address or id

	time.sleep(3)

	password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
	password.send_keys('xxxx') # insert password

	time.sleep(3)

	login = driver.find_element_by_xpath('//*[@id="btn-primary"]')
	login.click()

	time.sleep(3)

	search = driver.find_element_by_xpath('//*[@id="main-search-box"]')
	search.send_keys('python programmer')

	time.sleep(3)

	button = driver.find_element_by_xpath('//*[@id="global-search"]/fieldset/button')
	button.click()

	time.sleep(3)

	people = driver.find_element_by_xpath('//*[@id="search-types"]/div/ul/li[2]/a')
	people.click()	

	# driver.quit()

	return driver



def get_detail_link(driver):

	soup = BeautifulSoup(driver.page_source, 'lxml')	

	for a in soup.find_all('a', class_ = 'result-image'):
		print a['href']
	
	driver.quit()


get_detail_link( login_and_search() )
