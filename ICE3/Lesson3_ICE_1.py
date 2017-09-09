# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:07:00 2017

@author: Spencersun
"""

import requests
from bs4 import BeautifulSoup
import os

html = requests.get("https://en.wikipedia.org/wiki/Music_(disambiguation)") 
plain_text = html.text
soup = BeautifulSoup(plain_text, "html.parser")
print (soup)
result_list = soup.findAll('div', {'class': "mw-search-result-heading"})
for div in result_list:
    link = div.find('a')
    href = "https://en.wikipedia.org"+link.get('href')
    if (link.get('href').startswith("http")):
        href=link.get('href')
        get_data(href)


body = soup.find('div', {'class': 'mw-parser-output'})
print(body.text)
