# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:18:41 2020

@author: ichaddha
"""


import pandas as pd


import requests
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import csv
import time

items = pd.read_csv(r"C:\Users\ichaddha\Documents\URLs.csv")
book_info = []
for i in items.URL:
    URL = "https://www.barnesandnoble.com" + i
    page = urlopen(URL)
    soup = BeautifulSoup(page, "lxml")
    
    items2 = soup.select("#ProductDetailsTab")
    
    res = []
    res.append(str(items2))
        
    items2=pd.DataFrame({"raw_code": res})
    
    items2["raw_code"] = items2.raw_code.astype(str)
    items2["raw_code"][0]
    
    items2["publisher"] = items2.raw_code.str.split('"publisher">').str[1]
    items2["publisher"] = items2.publisher.str.split('</span>',1).str[0]
    
    items2["date"] = items2.raw_code.str.split('Publication date:</th>\n<td>').str[1]
    items2["date"] = items2.date.str.split('</td>\n',1).str[0]
   
    items2["pages"] = items2.raw_code.str.split('Pages:</th>\n<td>').str[1]
    items2["pages"] = items2.pages.str.split('</td>',1).str[0]
    
    items2["Sales_rank"] = items2.raw_code.str.split('Sales rank:</th>\n<td>').str[1]
    items2["Sales_rank"] = items2.Sales_rank.str.split('</td>',1).str[0]
    
    items2["URL"]= i
    
    book_info.append(items2)
    time.sleep(2.4)

book_info = pd.concat(book_info)

books_df = items.merge(book_info, how= "left",on = "URL")
books_df.to_csv(r"C:\Users\ichaddha\Documents\Book_Info.csv")
