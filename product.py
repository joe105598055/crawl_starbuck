from bs4 import BeautifulSoup
import requests
import re
from utils import download_image

BASE_URL = "https://bkmgr.starbucks.com.tw"

def is_product_link(link):
    regex = "^/products/food/product.jspx\?id"
    return bool(re.search(regex,link.get("href")))

def get_detail(product_link):
    product = {}
    response = requests.get(product_link)
    soup = BeautifulSoup(response.text, "html.parser")

    product['name'] = soup.find("h1",{'class':'title_cn'}).text
    origin_img = BASE_URL + soup.find('div',{'class':'image_block'}).find('img').get('src')
    product['price'] = int(soup.find("h3",{'class':'price'}).text.replace("起",""))
    product['introduction'] = soup.find("div",{'class':'info'}).text.replace('\n', '')
    product['imgUrl'] = 'https://storage.googleapis.com/online-order-9cb97.appspot.com/product/' + product['name'] + '.jpg'
    download_image(product['name'],origin_img)
    print(product)
    return product

DEFAULT_OPTION = [
    {
      "name": "大小",
      "optionItem": [
        {
          "name": "大",
          "price": 30
        },
        {
          "name": "中",
          "price": 20
        },
        {
          "name": "小",
          "price": 10
        }
      ]
    },
    {
      "name": "甜度",
      "optionItem": [
        {
          "name": "全糖",
          "price": 30
        },
        {
          "name": "半糖",
          "price": 20
        },
        {
          "name": "少糖",
          "price": 10
        }
      ]
    }
  ]

def get_products(category_url,categoryId):
    target_url = BASE_URL + category_url
    # 連結網站
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    product_links = list(filter(is_product_link,links))[0:2]

    result = []

    for prod in product_links:
        detail = get_detail(BASE_URL + prod.get('href'))
        detail['categoryId'] = categoryId
        detail['option'] = DEFAULT_OPTION
        result.append(detail)

    return result


	

