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
import re

items = pd.read_csv(r"C:\Users\ichaddha\Documents\URLs.csv")
book_info = []
female = r'\bher\b|\bshe\b|\bwoman\b|\bherself\b'
male = r'\bhim\b|\bhis\b|\bhe\b|\bman\b|\bhimself\b'
for i in items.URL:
    URL = "https://www.barnesandnoble.com" + i
    page = urlopen(URL)
    soup = BeautifulSoup(page, "lxml")
    ###getting product details
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
    items2.drop(columns=["raw_code"], inplace=True)
    items2["URL"]= i
    ### author info
    items3 = soup.select("#MeetTheAuthor")
    
    res = []
    res.append(str(items3))
        
    items3=pd.DataFrame({"raw_code": res})
    
    items3["raw_code"] = items3.raw_code.astype(str)
    
    items3["author_info"] = items3.raw_code.str.split('text--medium').str[1]
    items3["author_info"] = items3.author_info.str.split('</div>',1).str[0]
    
    if  bool(re.search(female, items3["author_info"][0],re.IGNORECASE)):
        items3["assumed_author_gender"] = "F"
    elif bool(re.search(male, items3["author_info"][0],re.IGNORECASE)):
        items3["assumed_author_gender"] = "M"
    else:
        items3["assumed_author_gender"] = "Unknown"
    items3.drop(columns=["raw_code"], inplace=True)
    items_fin = pd.concat([items2, items3], axis=1)
    book_info.append(items_fin)
    time.sleep(2.4)

book_info = pd.concat(book_info)

books_df = items.merge(book_info, how= "left",on = "URL")
books_df.drop(columns=["raw_code", "Prefix"], inplace=True)
books_df.to_csv(r"Book_Info.csv")
