from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import os

urls = [
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-01-09.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-10-14.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-15-19.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-20-29.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-30-34.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-35-39.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-40-45.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-46-56.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-60-75.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-76-80.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-81-85.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-86-94.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-102-111.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-113-128.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-131-135.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-136-140.zip',
    'https://outworldz.com/Secondlife/Posts/CMU/cmuconvert-daz-141-144.zip'
]

for url in urls:
    print("Downloading " + os.path.basename(url) + "...")
    with urlopen(url) as zip_resp:
        with ZipFile(BytesIO(zip_resp.read())) as zfile:
            zfile.extractall('./CMU-Data/' + os.path.basename(url)[:len(os.path.basename(url)) - 4])
