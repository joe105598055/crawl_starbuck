# -*- coding: utf-8 -*-
from category import get_categories
from product import get_products
from pathlib import Path
import shutil
import json

shutil.rmtree('./data',ignore_errors=True)
Path("./data").mkdir(parents=True, exist_ok=True)

categories = get_categories()
# get_products('/products/food/view.jspx?catId=74')

result = []
idx = 1
for category in categories:
    # {'category': '星早餐', 'url': '/products/food/view.jspx?catId=77'}
    categoryId = "c" + str(idx)
    product_list = get_products(category['url'],categoryId)
    result = result + product_list
    idx = idx + 1 

print(result)

with open('data.json', 'w',encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)