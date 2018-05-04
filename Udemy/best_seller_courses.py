from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def log_In():

	driver = webdriver.Chrome(r'C:\Users\Mohammed Innat\Downloads\Compressed\chromedriver_win32\chromedriver.exe')
	driver.get('https://www.udemy.com/join/login-popup/?displayType=ajax&xref=wish&courseId=67640&returnUrlAfterLogin=/russian-for-beginners-1/?courseId=67640%26xref=wish&display_type=popup')

	email = driver.find_element_by_xpath('//*[@id="id_email"]')
	email.send_keys('innat1994@gmail.com')


	password = driver.find_element_by_xpath('//*[@id="id_password"]')
	password.send_keys('udemy 1994')

	login = driver.find_element_by_xpath('//*[@id="submit-id-submit"]')
	login.click()

	driver.maximize_window()
	# search = driver.find_element_by_xpath('//*[@id="q"]')
	# search.send_keys('Machine Learning')

	# button = driver.find_element_by_xpath('//*[@id="searchbox"]/div/span/span/button')
	# button.click()
	return driver

def operation(driver):
	categoriy = driver.find_element_by_xpath('//*[@id="udemy"]/div[1]/div[3]/div/div/div[1]/a')
	categoriy.click()


	soup = BeautifulSoup(driver.page_source , 'lxml')
	print(soup.prettify())

	for item in soup.find_all('a' , class_ = 'c_topic'):
		print(item.text)

	driver.quit()

if __name__ == '__main__':
	operation(log_In())