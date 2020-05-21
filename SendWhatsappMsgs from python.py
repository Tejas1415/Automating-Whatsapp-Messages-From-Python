# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:23:53 2020

@author: Tejas
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

## Install Chrome Driver Automatically and open that.
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

## Open Whatsapp
driver.get("https://web.whatsapp.com/")

## Search by class name
search = driver.find_element_by_class_name("_251VP")


## Search for the name
search[0].send_keys("myself"+Keys.ENTER)

search = driver.find_element_by_class_name("_251VP")

## Send the following message
search[1].send_keys("Yo, Python says Hi"+Keys.ENTER)





