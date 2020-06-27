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

import random

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

    def parser(self, resp, city):
        try:
            # 标题
            # title_result = resp.html.xpath(
            #     '//*[@id="media-wrapper"]/div[2]/div/a/h1/text()')
            title_result = resp.html.xpath(
                '//div[@class="title"]/a/h1/text()')
            title = title_result[0] if title_result else None

            # 地址
            address_result = resp.html.xpath(
                '//*[@id="media-wrapper"]/div[2]/ul/li[1]/span/text()')
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

            # 景点开放时间
            open_time_result = resp.html.xpath('//li[@class="time"]/span/text()')
            open_time = ' '.join(open_time_result) if theme_result else None

            # 门票信息
            ticket_information_result = resp.html.xpath('//li[@class="promise"]/div/text()')
            ticket_information = ' '.join(ticket_information_result) if theme_result else None

            # 门票价格
            ticket_price_restlt = resp.html.xpath('//div[@class="price-box"]/span/text()')
            ticket_price = ' '.join(ticket_price_restlt) if theme_result else None

            # 图片
            img_result = resp.html.xpath('//*[@id="tFocus-pic"]/li/a/img/@src')
            img_result2 = resp.html.xpath('//*[@id="tFocus-pic"]/li/img/@src')
            img_result = (img_result or img_result2)
            if img_result:
                img_url = img_result[0]
                resp = requests.get('https:{}'.format(img_url))

                if not os.path.exists(city):    #如果data下文件夹不存在city名称的文件夹，则创建city文件夹
                    os.makedirs(city)
                folder_name = '.\\' + city + '\\{}.jpg'
                with open(folder_name.format(title), 'wb') as f:
                    f.write(resp.content)

            count = random.randint(300,400)
            stars = random.randint(2,5)
            return title, address, city, theme, introduce, traffic_guide, open_time, ticket_information, ticket_price ,count, count, stars

        except Exception as e:
            print(traceback.format_exc())

    def save_data(self, data, city):
        try:
            if not os.path.exists('data'):  # 如果不存在data名称的文件夹，则创建data文件夹
                os.makedirs('data')

            df = pd.DataFrame(data)
            file_name = '.\\data\\' +city +'.csv'
            if os.path.exists(file_name):
                df.to_csv(file_name, mode='a', index=False, na_rep='NA',
                          header=False, encoding='gbk')
            else:
                df.to_csv(file_name, mode='a', index=False, na_rep='NA',
                          header=['title', 'address', 'city','theme', 'introduce', 'traffic_guide', 'open_time', 'ticket_information', 'ticket_price', 'ticket_total', 'ticket_surplus','stars'], encoding='gbk')
        except Exception as e:
            print(traceback.format_exc())

    def main(self, url, city):
        try:
            session = HTMLSession()
            resp = session.get(url, headers=headers)
            base_data = self.parser(resp,city)
            data = [base_data]
            self.save_data(data,city)
        except Exception as e:
            print(traceback.format_exc())


def run():
    city = ['桂林','南宁','梧州','柳州','百色','河池','北海','防城港','贺州','玉林','贵港','钦州','崇左','来宾']
    city_pinyin = ['guilin','nanning','wuzhou','liuzhou','baise','hechi','beihai','fangchenggang','hezhou','yulin','guigang','qinzhou','chongzuo','laibing']
    city_pages = [14, 6, 5, 5, 4, 4, 4, 3, 3, 2, 2, 2, 2, 1]

    q_url = "https://www.cncn.com/piao/"
    h_url = ".htm"

    for k in range(0, len(city)):   #city，爬取city[k]城市中的景点；来宾不爬，只有1页，去掉'/1s'后可爬
        # for i in range(1, city_pages[k]+1):       #爬取每个城市所有景点，city_pages[k]为该城市存在n页
        for i in range(1, 2):  # 爬取每个城市所有景点，city_pages[k]为该城市存在n页
            url_first = q_url +city_pinyin[k] +'/1s'+ str(i) + h_url
            html = requests.get(url_first, headers1)
            dom = etree.HTML(html.text)
            h_url_xqy = dom.xpath('//div[@class="list_top"]/a/@href')
            for j in h_url_xqy:
                time.sleep(1)
                url_xqy = "https://www.cncn.com" + j
                print(url_xqy)
                crawler = Crawler()
                crawler.main(url_xqy,city[k])


if __name__ == '__main__':
    run()
