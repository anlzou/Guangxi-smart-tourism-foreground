#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import time

import requests
from requests_html import HTMLSession
import pandas as pd
import traceback

import os
import time
from lxml import etree
import requests

headers1 = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie':  'UM_distinctid=172b674e5f71cb-034c5dfe424061-3a365305-1fa400-172b674e5f8848; PHPSESSID=4gsduu0v6tmi1lkbsf8cp7kej0; local_zone=320100%7Cnanjing%7C%C4%CF%BE%A9%7C58238; Hm_lvt_d64174522c86449826babe56fb2a88ff=1592199015; CNZZDATA1089612=cnzz_eid%3D725595362-1592200519-https%253A%252F%252Fguilin.cncn.com%252F%26ntime%3D1592200519; Hm_lpvt_d64174522c86449826babe56fb2a88ff=1592203476',
    'pragma': 'no-cache',
    # 'referer':  'https://beihai.cncn.com/jingdian/beihai/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie':  'UM_distinctid=172b674e5f71cb-034c5dfe424061-3a365305-1fa400-172b674e5f8848; PHPSESSID=4gsduu0v6tmi1lkbsf8cp7kej0; local_zone=320100%7Cnanjing%7C%C4%CF%BE%A9%7C58238; Hm_lvt_d64174522c86449826babe56fb2a88ff=1592199015; CNZZDATA1089612=cnzz_eid%3D725595362-1592200519-https%253A%252F%252Fguilin.cncn.com%252F%26ntime%3D1592200519; Hm_lpvt_d64174522c86449826babe56fb2a88ff=1592203476',
    'pragma': 'no-cache',
    # 'referer':  'https://beihai.cncn.com/jingdian/beihai/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',

}


class Crawler(object):

    def parser(self, resp):
        try:
            # 标题
            title_result = resp.html.xpath('//*[@id="media-wrapper"]/div[2]/div/a/h1/text()')
            title = title_result[0] if title_result else None

            # 地址
            address_result = resp.html.xpath('//*[@id="media-wrapper"]/div[2]/ul/li[1]/span/text()')
            address = address_result[0] if address_result else None

            # 景区主题
            theme_result = resp.html.xpath('//*[@id="J-MediaLabel"]/a/text()')
            theme = ' '.join(theme_result) if theme_result else None

            # 景点介绍
            introduce = ''
            contents = resp.html.xpath('//*[@id="J-Jdjj"]/div/p')
            contents_1 = resp.html.xpath('//*[@id="J-Jdjj"]/div/text()')
            if contents:
                for i in contents:
                    introduce += i.text.replace('\xa0', ' ').strip() + '\n'
                    print(introduce)
            elif contents_1:
                introduce = contents_1[0].strip()

            # 交通指南
            traffic_guide = None
            t_result = resp.html.xpath('//*[@id="J-Jtzn"]/div[3]/text()')
            if len(t_result) >= 2 and t_result[1]:
                traffic_guide = t_result[1].replace('\xa0', '').strip()

            # 图片
            img_result = resp.html.xpath('//*[@id="tFocus-pic"]/li/a/img/@src')
            if img_result:
                img_url = img_result[0]
                resp = requests.get('https:{}'.format(img_url))
                with open(r'.\imgs\{}.jpg'.format(title), 'wb') as f:
                    f.write(resp.content)

            return title, address, theme, introduce, traffic_guide
        except Exception as e:
            print(traceback.format_exc())

    def save_data(self, data):
        try:
            df = pd.DataFrame(data)
            if os.path.exists(r'.\test.csv'):
                df.to_csv(r'.\test.csv', mode='a', index=False, na_rep='NA',
                          header=False, encoding='gbk')
            else:
                df.to_csv(r'.\test.csv', mode='a', index=False, na_rep='NA',
                          header=['title', 'address', 'theme', 'introduce', 'traffic_guide'], encoding='gbk')
        except Exception as e:
            print(traceback.format_exc())

    def main(self, url):
        try:
            # url = 'https://www.cncn.com{}'.format(id
            # )
            session = HTMLSession()
            resp = session.get(url, headers=headers)
            base_data = self.parser(resp)
            data = [base_data]
            self.save_data(data)
        except Exception as e:
            print(traceback.format_exc())


def run():
    q_url = "https://www.cncn.com/piao/guangxi/1s"
    h_url = ".htm"
    h_xqy2 = '/profile'
    for i in range(1, 2):
        url_first = q_url + str(i) + h_url
        # print(url_first)
        html = requests.get(url_first, headers1)
        dom = etree.HTML(html.text)
        h_url_xqy = dom.xpath('//div[@class="list_top"]/a/@href')
        for j in h_url_xqy:
            time.sleep(1)
            url_xqy = "https://www.cncn.com" + j
            print(url_xqy)
            crawler = Crawler()
            crawler.main(url_xqy)


if __name__ == '__main__':
    run()