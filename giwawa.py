# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:04:42 2022

@author: tseng.yu
"""
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--incognito")
ua = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
opts.add_argument("user-agent={}".format(ua))

driver = webdriver.Chrome("C:\\chromedriver",chrome_options=opts)
driver.get("http://60.191.148.66/seeyon/index.jsp")
print(driver.page_source)

time.sleep(10)

df = pd.read_excel("C:\\Users\lawrence1118\Desktop\Account\帳號.xls")
print(df)

for i in range(1000):
    print(df['登录名'][i+1])
    user = driver.find_element("xpath",'//*[@id="login_username"]')
    password = driver.find_element("xpath",'//*[@id="login_password"]')
    user.send_keys(df['登录名'][i+1])
    password.send_keys(df['登录名'][i+1])
    button = driver.find_element("xpath",'//*[@id="login_button"]')
    button.click()
    user = driver.find_element("xpath",'//*[@id="login_username"]')
    password = driver.find_element("xpath",'//*[@id="login_password"]')
    user.send_keys(df['登录名'][i+1])
    password.send_keys('123456')
    button = driver.find_element("xpath",'//*[@id="login_button"]')
    button.click()
    #driver.refresh()
   # time.sleep(1)"""



