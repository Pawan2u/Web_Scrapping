#          <a> anchor tag

# Finding ALl the Links on the Webpage is Easy!
#           Not at all, It is not like one Scrapper for all
#           websites is gonna work.
# Because all the websites have different & we need to understand & analyze 
# all the structures accordindingly to that write Scrappers

# YES Little bit generalized scrapper for most of the websites
# But eventually we have to customized the scrapper 

"""
    Find the all links from an websites 'https://xyz.com'
    if there is # that means no link ignore this not print at all
    if link start from ./about --> https://xyz.com/about

"""

import requests
import bs4

res = requests.get('https://abcxyz.in/')

soup = bs4.BeautifulSoup(res.text,'lxml')
'''
for link in soup.find_all('a',href=True):  # Just to be safe if href is True, otherwise not
    print(link['href'])
'''
for link in soup.find_all('a',href=True):
    if link['href'] == '/#':
        pass
    else:
        if link['href'].startswith('/'):
            print('https://xyz.com'+link['href'])
        else:
            print(link['href'])


