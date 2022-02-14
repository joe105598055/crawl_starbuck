import pathlib
import shutil
from utils import resize_image

shutil.rmtree('./resize',ignore_errors=True)

for p in pathlib.Path('data').iterdir():
    if p.is_file():
        print(str(p))
        resize_image(str(p),150)