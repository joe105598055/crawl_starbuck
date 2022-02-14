import requests
from PIL import Image
from pathlib import Path
from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/joehuang/online-order-9cb97-firebase-adminsdk-23io1-f633cbf71f.json"

def download_image(name,url):
	name = name.replace("/","_")
	res = requests.get(url, allow_redirects=True)
	f = open('./data/' + name + '.jpg', 'wb').write(res.content)

def resize_image(source):
    RESIZE_DIR = "./resize"
    Path(RESIZE_DIR).mkdir(parents=True, exist_ok=True)
    basewidth = 10
    img = Image.open(source)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(RESIZE_DIR +'/' + source.split("/")[-1], 'JPEG')

def upload_image(source):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('online-order-9cb97.appspot.com')
    filename = source.split("/")[-1]
    blob = bucket.blob("test/" + filename)
    ## For slow upload speed
    # storage.blob._DEFAULT_CHUNKSIZE = 2097152 # 1024 * 1024 B * 2 = 2 MB
    # storage.blob._MAX_MULTIPART_SIZE = 2097152 # 2 MB
    with open("resize/" + filename, 'rb') as f:
        blob.upload_from_file(f,True,None,"image/jpeg")
        target = bucket.blob("test/" + filename)
        target.make_public()
        print(target.public_url)