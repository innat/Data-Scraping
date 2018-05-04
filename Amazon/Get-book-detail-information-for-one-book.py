# strategy

# soup --> ISBN table id="productDetailsTable"
# 					find_all li tag --> get 4th li

#  	 --> Detail --> iframe --> div.text


from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.amazon.com/Python-Programming-Introduction-Computer-Science/dp/1590282418/ref=sr_1_1?ie=UTF8&qid=1473731166&sr=8-1&keywords=python+programming'

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

table = soup.find('table', {'id':'productDetailsTable'})

all_li = table.find_all('li')

isbn = all_li[3].text.strip('ISBN-10: ')

print isbn

driver.switch_to_frame( driver.find_element_by_tag_name('iframe'))

soup = BeautifulSoup(driver.page_source,'lxml')

description = soup.find('div').text

print description

driver.quit()


