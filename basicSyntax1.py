# EXTRACT TITLE FROM WEBSITES

import requests
import bs4
import lxml

res = requests.get('https://abcxyz.in/')

soup = bs4.BeautifulSoup(res.text,'lxml')

t = soup.select('title')

print(t)

print(t[0])

print( t[0].getText() )