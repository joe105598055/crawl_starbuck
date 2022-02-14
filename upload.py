import pathlib
from utils import upload_image

flist = []
for p in pathlib.Path('resize').iterdir():
    if p.is_file():
        print(str(p))
        upload_image(str(p))