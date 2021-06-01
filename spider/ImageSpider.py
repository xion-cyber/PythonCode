#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
this program is used for downloading the images in the PEXELS website
author: YeYiqi
date: 2021-5-27
"""

import requests
import json
from bs4 import BeautifulSoup

headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

url_path = 'https://www.pexels.com/search/'
word = input('input the pictures you want to download: ')
url = url_path + word + '/'
wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
imgs = soup.select('article > a > img')
list = []
for img in imgs:
    photo = img.get('scr')
    list.append(photo)

path = 'C:/Users/1/Desktop/image/'

for item in list:
    data = requests.get(item, headers=headers)
    fp = open(path+item.split('?')[0][-10:], 'wb')
    fp.write(data.content)
    fp.close()