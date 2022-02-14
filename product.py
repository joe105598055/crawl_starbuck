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
    product['origin_img'] = BASE_URL + soup.find('div',{'class':'image_block'}).find('img').get('src')
    product['price'] = int(soup.find("h3",{'class':'price'}).text.replace("起",""))
    product['introduction'] = soup.find("div",{'class':'info'}).text.replace('\n', '')
    product['imgUrl'] = 'https://storage.googleapis.com/online-order-9cb97.appspot.com/test/' + product['name'] + '.jpg'

    download_image(product['name'],product['origin_img'])
    print(product)

    return product

def get_products(category_url):
    target_url = BASE_URL + category_url
    # 連結網站
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    product_links = list(filter(is_product_link,links))[0:10]

    result = []

    for prod in product_links:
        detail = get_detail(BASE_URL + prod.get('href'))
        result.append(detail)

    return result


	

