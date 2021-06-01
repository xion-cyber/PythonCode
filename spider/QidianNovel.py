#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
This program is used to download the novels' information in Qidian.com
author: YeYiqi
date: 2021-5-25
"""

import requests
import xlwt
from lxml import etree
import time

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

all_info_list = []

def get_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')

    for info in infos:
        title = info.xpath('div[2]/h4/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        style = style_1+'.'+style_2
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        introduce = info.xpath('div[2]/p[2]/text()')[0]
        word = info.xpath('div[2]/p[3]/span/text()')[0]
        info_list = [title, author, style, complete, introduce, word]
        all_info_list.append(info_list)
    time.sleep(1)

if __name__ == '__main__':
    urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page={}'.format
            (str(i)) for i in range(1, 6)]
    for url in urls:
        get_info(url)
        print(urls.index(url)+1, '页已下载')

    header = ['标题', '作者', '类型', '连载状况', '简介', '字数']
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    i = 1
    for list in all_info_list:
        j = 0
        for data in list:
            sheet.write(i, j, data)
            j += 1
        i += 1
    book.save('xiaoshuo.xls')
