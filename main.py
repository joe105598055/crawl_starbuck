from base64 import encode
from category import get_categories
from product import get_products
import json

categories = get_categories()
# get_products('/products/food/view.jspx?catId=74')

result = []
idx = 1
for category in categories:
    # {'category': '星早餐', 'url': '/products/food/view.jspx?catId=77'}
    product_list = get_products(category['url'])
    category['catId'] = "c" + str(idx)
    category['product_list'] = product_list
    result.append(category)
    idx = idx + 1 

print(result)

with open('data.json', 'w',encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)