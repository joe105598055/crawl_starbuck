# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage 

# # cred = credentials.Certificate("path/to/serviceAccountKey.json")
# cred = credentials.Certificate("./online-order-9cb97-firebase-adminsdk-23io1-f633cbf71f.json")
# app = firebase_admin.initialize_app(cred)

from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.get_bucket('online-order-9cb97.appspot.com')
blob = bucket.blob("test/舒肥雞肉蔬菜盅.jpg")

## For slow upload speed
# storage.blob._DEFAULT_CHUNKSIZE = 2097152 # 1024 * 1024 B * 2 = 2 MB
# storage.blob._MAX_MULTIPART_SIZE = 2097152 # 2 MB
with open("./data/test.jpg", 'rb') as f:
    blob.upload_from_file(f,True,None,"image/jpeg")
    target = bucket.blob("test/舒肥雞肉蔬菜盅.jpg")
    target.make_public()
    print(target.public_url)