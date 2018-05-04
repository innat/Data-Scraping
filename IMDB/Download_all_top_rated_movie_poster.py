
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


driver = webdriver.Chrome(executable_path = r'C:\Users\Mohammed Innat\Downloads\Compressed\chromedriver_win32\chromedriver.exe')
url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'
driver.get(url)


class flim():
	"""docstring for flim"""
	def __init__(self):
		self.rank = ''
		self.title = ''
		self.year = ''
		self.link = ''
		

def get_list():

	

	soup = BeautifulSoup(driver.page_source , 'lxml')
	table = soup.find('table' , class_ = 'chart')
	list_ = []


	for td in table.find_all('td' , class_ = 'titleColumn'):
		full_title = td.text.strip().replace('\n','').replace('      ','')

		rank = full_title.split('.')[0]
		title = full_title.split('.')[1].split('(')[0]
		year = full_title.split('(')[1][:-1]
		a = td.find('a')

		flim_list = flim()
		flim_list.rank = rank
		flim_list.title = title
		flim_list.year = year
		flim_list.link = a['href']

		list_.append(flim_list)

	driver.quit()	

	return list_


def download_poster(list_):

	driver = webdriver.Chrome(executable_path = r'C:\Users\Mohammed Innat\Downloads\Compressed\chromedriver_win32\chromedriver.exe')

	for flim in list_:
		

		# url = 'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=0W3MN13RKP4WZEAFAXBG&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'

		url = 'https://www.imdb.com/' + flim.link
		driver.get(url)

		soup = BeautifulSoup(driver.page_source , 'lxml')

		div = soup.find('div' , class_ = 'poster')
		a = div.find('a')

		url = 'http://www.imdb.com' + a['href']
		driver.get(url)
		soup = BeautifulSoup(driver.page_source , 'lxml')

		all_div = soup.find_all('div' , class_= 'pswp__zoom-wrap')
		all_img = all_div[1].find_all('img')

		print(all_img[1]['src'])

		with open(f'{flim.title}.jpg', 'wb') as f:
			f.write(requests.get(all_img[1]['src']).content)
 
	driver.quit()

download_poster(get_list())