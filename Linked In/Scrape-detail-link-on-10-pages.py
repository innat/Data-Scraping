# a class="result-image"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

def login_and_search():	

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

	time.sleep(3)

	search = driver.find_element_by_xpath('//*[@id="main-search-box"]')
	search.send_keys('python programmer')

	time.sleep(3)

	button = driver.find_element_by_xpath('//*[@id="global-search"]/fieldset/button')
	button.click()

	time.sleep(3)

	people = driver.find_element_by_xpath('//*[@id="search-types"]/div/ul/li[2]/a')
	people.click()

	return driver



def get_detail_link(link_list):

	detail_link = []

	for link in link_list:

		driver.get(link)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		for a in soup.find_all('a', class_ = 'result-image'):
			print a['href']
			detail_link.append(a['href'])

	return detail_link



def get_page_links():
	
	soup = BeautifulSoup(driver.page_source, 'lxml')	

	link_list = []

	# add the current link, page 1 to list
	link_list.append(driver.current_url)
	print driver.current_url

	ul = soup.find('ul', class_='pagination')

	# not get the final link
	for a in ul.find_all('a')[0:(len(ul.find_all('a'))-2)]:
		print 'https://www.linkedin.com' + a['href']
		link_list.append('https://www.linkedin.com' + a['href'])	

	print '\n'
	print '\n'
	print '\n'

	return link_list



########################################### MAIN ###################################

login_and_search()

get_detail_link(get_page_links())

driver.quit()

####################################################################################


