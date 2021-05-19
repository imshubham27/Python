from selenium import webdriver
import numpy as np
import time
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import urllib.request
import os
from selenium.webdriver.common.action_chains import ActionChains

l = []

wd = webdriver.Edge(r'C:\msedgedriver')
Initial_page = 1
last_page = 2  # CHANGE HERE TO VISIT MORE PAGES
for t in range(Initial_page, last_page):
    wd.get("https://www.carvana.com/cars?page={}".format(t))
    wd.maximize_window()
    wd.implicitly_wait(10)
    item1 = wd.find_element_by_xpath("/html/body")
    c = item1.get_attribute('innerHTML')
    soup = BeautifulSoup(c, 'html.parser')
    a = (soup.find_all(
        "a", {"class": "VehicleLinkstyles__StyledLink-sc-4bed30-0 gkBjLI"}))
    for i in range(len(a)):
        d = {}
        print(a[i]['href'])
        wd.implicitly_wait(5)
        wd.get("https://www.carvana.com/{}".format(a[i]['href']))
        wd.implicitly_wait(5)
        item1 = wd.find_element_by_xpath(
            "//div[@class='styles__MakeModelAndTrim-v7qvvn-8 YwKtb']")
        lis = (str(item1.text).split('\n'))
        wd.implicitly_wait(1)
        try:
            wd.find_element_by_xpath("//div[@id='spinnerMouseLayer']").click()
        except:
            continue
        wd.implicitly_wait(2)
        wd.find_element_by_xpath(
            '//div[@class="sc-fznBtT sc-fzobTh jEgRJw sc-qcrrk kCWYLZ"]/*[name()="svg"][@xmlns="http://www.w3.org/2000/svg"]').click()

        source1 = wd.find_element_by_xpath("//div[@id='spinnerMouseLayer']")
        os.makedirs("SPYNE\CAR_{}_{}".format(t, i))
        action = ActionChains(wd)
        z = 1
        e = 0.001
        for j in range(5):  # CHANGE HERE TO GET MORE ANGLE OF CAR
            print("J", j)
            action.click_and_hold(source1).move_by_offset(
                100+z, 100).pause(0.003+e).move_by_offset(50, 100).release().perform()
            z *= 1.2
            e += 0.00079
            wd.save_screenshot(
                r"SPYNE\CAR_{}_{}\screenshot_{}.png".format(t, i, j))
            print("Dragging & dropping test case successful\n")
        try:
            d["CAR BRAND"] = lis[0]
        except:
            d["CAR BRAND"] = "Not mentioned"
        try:
            d["CAR NAME"] = lis[1]
        except:
            d["CAR NAME"] = "Not mentioned"
        try:
            d["CAR MODEL"] = lis[2]
        except:
            d["CAR MODEL"] = "Not mentioned"
        print("D", d)
        l.append(d)
df = pd.DataFrame(l)
df.to_csv("Output.csv")
