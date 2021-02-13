
# pip install requests, pip install bs4, pip install lxml

import requests    # to use requests obj
import bs4         # BeautifulSoup 4 To extract info from texts

                   # request to the websites from where you want to do scrapping

res = requests.get('https://xyz.in/')

print(type(res))   # res is obj of requests, stores all the stuffs

print(res.text)    # stores entire webpage

                   # Not useful because need not the entire data
                   # So We only need to extract useful information from the text

                   # BeautifulSoup comes into the picture
                   
                   # (req obj, Tree xml)

soup = bs4.BeautifulSoup(res.text,'lxml')

print(type(soup))  # bs4 object


        

