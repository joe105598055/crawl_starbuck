import requests

def download_image(name,url):
	name = name.replace("/","_")
	res = requests.get(url, allow_redirects=True)
	f = open('./data/' + name + '.jpg', 'wb').write(res.content)
	