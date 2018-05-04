from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'C:\Users\Mohammed Innat\Downloads\Compressed\chromedriver_win32\chromedriver.exe')
url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'
driver.get(url)

soup = BeautifulSoup(driver.page_source , 'lxml')



class flim():
	"""docstring for flim"""
	def __init__(self):
		self.rank = ''
		self.title = ''
		self.year = ''
		self.link = ''
		

list_ = []


table = soup.find('table' , class_ = 'chart')

def get_list():

	for td in table.find_all('td' , class_ = 'titleColumn'):
		full_title = td.text.strip().replace('\n','').replace('      ','')

		rank = full_title.split('.')[0]
		title = full_title.split('.')[1].split('(')[0]
		year = full_title.split('(')[1][:-1]

		flim_list = flim()
		flim_list.rank = rank
		flim_list.title = title
		flim_list.year = year

		list_.append(flim_list)

		driver.quit()	

	return list_


flim_list = get_list()

for t in flim_list:
	print(t.rank)
	print(t.title)
	print(t.year)
	print(t.link)
	print('\n')