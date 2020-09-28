# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:43:57 2020

@author: ichaddha
"""

##Selenium tutorial
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:\Users\ichaddha\Downloads\chromedriver.exe")

driver.get("https://www.goodreads.com/genres/autobiography")
link = driver.find_element_by_link_text("Too Much and Never Enough: How My Family Created the World's Most Dangerous Man")
driver.find_element_by_css_selector('.bookImage').get_attribute('href')

elem = driver.find_element(By.CSS_SELECTOR, "img[src='https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1594640055l/54081499._SY475_.jpg']").click()
elem.click()
