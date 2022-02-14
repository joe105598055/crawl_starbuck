import pathlib
from utils import resize_image

flist = []
for p in pathlib.Path('data').iterdir():
    if p.is_file():
        print(str(p))
        resize_image(str(p))