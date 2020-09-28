# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:36:15 2020

@author: ichaddha
"""


from selenium import webdriver

import pandas as pd


import requests
from bs4 import BeautifulSoup

URL = 'https://www.barnesandnoble.com/b/new-releases/_/N-1oyg?Nrpp=40&Ns=P_Publication_Date%7C1&page=1'
page = requests.get(URL)

soup = BeautifulSoup(page.text)


items2 = soup.select(".bnBadgeHere")

res = []
for i in items2:
    res.append(str(i))
    
items2=pd.DataFrame({"raw_code": res})
items2["raw_code"] = items2.raw_code.astype(str)
items2["raw_code"][0]
items2["book"] = items2.raw_code.str.split('Title:').str[1]
items2["book"] = items2.book.str.split(':',1).str[0]
items2["author"] = items2.raw_code.str.split('Author:').str[1]
items2["author"] = items2.author.str.split('"',1).str[0]
items2["author"][0]
items2["URL"] = items2.raw_code.str.split('data-quickview-url="').str[1]
items2["URL"] = items2.URL.str.split('"',1).str[0]
items2["Prefix"] = "https://www.barnesandnoble.com"
