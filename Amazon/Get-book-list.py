# python programing
# soup --> find ul id = s-results-list-atf
# 			findall li class = s-result-item celwidget
# 				findall a and get second a tag
# 						a['href']
# 						a.text

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')



