
from selenium import webdriver
from bs4 import BeautifulSoup 

driver = webdriver.Chrome(executable_path = r'C:\Users\Mohammed Innat\Downloads\Compressed\chromedriver_win32\chromedriver.exe')

driver.get('http://python.org')

html_doc = driver.page_source

soup = BeautifulSoup(html_doc,'lxml')

print(soup.prettify())

driver.quit()
