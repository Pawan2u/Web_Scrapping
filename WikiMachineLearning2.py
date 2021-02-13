# GET ALL THE DATA from CONTENT SECTION

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('toclevel-1')  # 'toclevel' is a class name of elements  from the html tags
                           #  Just Analyzing by Inspect

for i in soup.select('.toclevel-1'):
    print(i.text)