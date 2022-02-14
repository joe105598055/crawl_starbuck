##### Env
pipenv shell 
C:\Users\joe\firebase_auth\online-order-9cb97-firebase-adminsdk-23io1-f633cbf71f.json
##### Quick start
```
// dumps all data from starbucks and download image 
$ python dump.py

// resize all file from ./data to ./resize
$ python resize.py 

// upload to firebase storage
$ python upload.py
```
##### Outline
- menu -> category -> product
- 進入link爬取 1.圖片 2.名稱 3.介紹 4.價錢

https://firebase.google.com/docs/storage/gcp-integration#apis


##### Todo 
- resize image
- upload all resized image to firebase storage
- group final data


##### Ref
[Set 'GOOGLE_APPLICATION_CREDENTIALS' environment variable](https://cloud.google.com/docs/authentication/getting-started).


##### Note
✔ Successfully created virtual environment! 
Virtualenv location: /Users/joehuang/.local/share/virtualenvs/crawl_starbuck-Kr1KoODs