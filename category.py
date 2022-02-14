# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

def is_catId_link(link):
    regex = "^/products/food/view.jspx\?catId="
    return bool(re.search(regex,link.get("href")))

def get_categories():
    menu_url = "https://bkmgr.starbucks.com.tw/coffee/menu.serx?currUrl=V2"

    # 連結網站
    response = requests.get(menu_url)
    soup = BeautifulSoup(response.json()["subMenu"], "html.parser")

    links = soup.find_all("a")

    catId_links = map(lambda x: {'category':x.text,'url':x.get('href')},filter(is_catId_link,links))

    # 取n比 [0:n]
    result = list(catId_links)[0:1]

    return result


	

