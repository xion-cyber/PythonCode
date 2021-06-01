#!/user/bin/env python
# -*- coding:utf-8 -*-

"""
Thie program is used to get the top 250 in douban.com
author: YeYiqi
date: 2021-5-22
"""

from lxml import etree
import requests
import csv
import time

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

fp = open('C:/Users/1/Desktop/doubanTop250.csv', 'w+', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 'rate', 'comment'))

def get_info(url):
    """
    this function is used to get the books information in
    one web page, and then write then into the csv file.
    But sometimes the information is incomplete, so you
    need try and except to prevent overflow.
    :param url:
    :return:
    """
    html = requests.get(url, headers=headers)
    # request web page data
    selector = etree.HTML(html.text)
    # parse and extract data
    infos = selector.xpath('//tr[@class="item"]')
    # find all the items
    for info in infos:
        name = info.xpath('td[2]/div[1]/a/@title')[0]
        url = info.xpath('td[2]/div[1]/a/@href')[0]
        book_infos = info.xpath('td[2]/p/text()')[0].split('/')
        author = book_infos[0]
        try:
            publisher = book_infos[-3]
        except:
            publisher = ''
        date = book_infos[-2]
        price = book_infos[-1]
        rate = info.xpath('td[2]/div[2]/span[2]/text()')[0]
        try:
            comment = info.xpath('td[2]/p/span/text()')[0]
        except:
            comment = ''
        # this opreation is used to prevent the crash
        writer.writerow((name, url, author, publisher, date, price, rate, comment))

if __name__ == '__main__':
    urls = ['https://book.douban.com/top250?start={}'.format
            (str(i)) for i in range(0, 250, 25)]
    # generate the url links, total 10
    for url in urls:
        get_info(url)
        print(urls.index(url)+1,'页已下载\n')
        time.sleep(1)

    fp.close()