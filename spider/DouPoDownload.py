#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
DouPoDownload.py
~~~~~~~~~~~~~~~~
This program is used to download the full text of 《斗破苍穹》
author: YeYiqi
date: 2021-5-22
"""

import requests
import re
import time

headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

f = open('C:/Users/1/Desktop/doupo.txt', 'a+')

def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        # if status_code is 200 it's normal, or something goes wrong
        titles = re.findall('<h1>(.*?)</h1>', res.content.decode('utf-8'), re.S)
        # search all the titles
        f.write(titles[0] + '\n')
        # write the title into the txt file
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'), re.S)
        # search the content
        for content in contents:
            f.write(content + '\n')
            # write the content into the text file
    else:
        pass
        # if something goes wrong, just pass

if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format
            (str(i)) for i in range(1,1646)]
    # generate all the url links
    for url in urls:
        get_info(url)
        print(url+'已下载')
        # time.sleep(1)
        # if necessary, you can set the sleep time to prevent the failure to capture text
    f.close()

