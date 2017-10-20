#!/usr/bin/env python
# encoding=utf-8

import requests
import re
import codecs
from bs4 import BeautifulSoup
from openpyxl import Workbook
wb = Workbook()
dest_filename = '上海交易所.xlsx'
ws1 = wb.active
ws1.title = "上海交易所"

DOWNLOAD_URL = 'http://www.sse.com.cn/'

def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

def get_li(doc):
    s_date = []
    s_title = []
    soup = BeautifulSoup(doc, 'html.parser')
    div = soup.find('div', class_='row-two')
    sse_list_1 = div.find('div', class_="sse_list_1")
    for i in sse_list_1.find_all('dd'):
        sse_title = i.find('a')
        s_title.append(sse_title.get_text())

    return s_title,None
    # name = []  # 名字
    # star_con = []  # 评价人数
    # score = []  # 评分
    # info_list = []  # 短评


def main():
    url = DOWNLOAD_URL
    title = []
    while url:
        doc = download_page(url)
        s_title,url = get_li(doc)
        title = title + s_title
    for (i, m) in zip(s_title, s_title):
        col_A = 'A%s' % (s_title.index(i) + 1)
        ws1[col_A] = i

    wb.save(filename=dest_filename)

if __name__ == '__main__':
    main()