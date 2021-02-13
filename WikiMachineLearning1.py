# Analyze the things for which you want to Scrapping
# wikipedia : 'Machine Learning'

# Find all the links
# Find all the headings

"""
       1. What to do?
       2. Analyze CSS of Website
       3. Check Inspect

       Python Script
        
            step 1. Use a requests, send the requests to the website
                    requests obj stores data

            step 2. Convert that Obj into BeautifulSoupn obj 
                    So that we can run all functions and everything 
"""

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup = bs4.BeautifulSoup(res.text,'lxml')

#soup.select('title')
#soup.select('div')
#soup.select('h1')
#soup.select('h1 > span')
#soup.select('#id')
#soup.select('.class')
soup.select('.mw-headline')

for i in soup.select('.mw-headline'):
    print(i.text)