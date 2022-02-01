from bs4 import BeautifulSoup
import requests
import re


# 連結網站
response = requests.get(
	"https://www.starbucks.com.tw/products/drinks/view.jspx?catId=4")
	

# HTML原始碼解析
soup = BeautifulSoup(response.text, "html.parser")

# 商品名稱
titleNames = []
titles = soup.find_all("h1", {"class": "title_cn"})
for idx,title in enumerate(titles):
	print(idx,title.string)  # 取得標題文字
	titleNames.append(title.string)

print(titleNames)
urls = soup.find_all(src=re.compile(".jpg"))
# 商品圖片
for idx,url in enumerate(urls):
	print(idx,url.get('src'))  # 取得標題文字
	img_url = 'https://www.starbucks.com.tw/' + url.get('src')
	filename = titleNames[idx] + '.jpg'
	r = requests.get(img_url, allow_redirects=True)
	open(filename, 'wb').write(r.content)
	