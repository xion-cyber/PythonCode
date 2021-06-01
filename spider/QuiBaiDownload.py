#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
This program is used to download the text of 糗事百科
author: YeYiqi
date: 2021-5-22
"""

import requests
import re
import time

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

f = open('C:/Users/1/Desktop/qiushi.txt', 'w+')

def judgement_sex(class_name):
    """return the user's gender"""
    if class_name == 'manIcon':
        return '男'
    else:
        return '女'

def get_info(url):
    """Get the content and write them into the txt file"""
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender manIcon">(.*?)</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>.*?</div>', res.content.decode('utf-8'), re.S)
    laughs = re.findall('<i class="number">(.*?)</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i>', res.text, re.S)
    for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        try:
            f.write('id号码：'+id.strip()+'\n')
            f.write('等级：'+level+'\n')
            f.write('性别：'+judgement_sex(sex) + '\n')
            f.write('内容:'+content.strip()+'\n')
            f.write('觉得好笑：'+laugh+'\n')
            f.write('评论数：'+comment+'\n\n')
        except:
            pass

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format
            (str(i)) for i in range(1,31)]
    for url in urls:
        get_info(url)
        print('第',urls.index(url)+1,'页已下载\n')
    f.close()