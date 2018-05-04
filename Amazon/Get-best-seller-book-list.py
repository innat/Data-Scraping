from bs4 import BeautifulSoup
from selenium import webdriver
import time

def get_python_book_list():
	
	book_list = []

	driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	
	for page in range(1,6):

		url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books#{0}'.format(page)

		print url
		
		driver.get(url)

		time.sleep(3)
		
		soup = BeautifulSoup(driver.page_source, 'lxml')

		print len(soup.find_all('div',class_ = 'zg_itemImmersion'))

		for div in soup.find_all('div',class_ = 'zg_itemImmersion'):
			# print div.find('div', class_ = 'zg_title').text
			book_list.append(div.find('div', class_ = 'zg_title').text)

	for book in book_list:
		print book	

	return book_list

get_python_book_list()