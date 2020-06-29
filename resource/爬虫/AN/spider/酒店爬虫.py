from requests_html import HTMLSession
import pandas as pd
import traceback

import os
import time
from lxml import etree
import requests

import datetime


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

    def parser(self, resp,city):
        try:
            # 景点名称
            title_result = resp.html.xpath(
                '//div[@class="list_hotel mt20"]/div/strong/text()')
            title = title_result[0] if title_result else None
            print("======="+city+"：【"+title+"】=======")

            # 酒店名称
            hotels_result = resp.html.xpath('//div[@class="text_con"]/p/text()')
            for i in hotels_result:
                print(i)

            # 酒店价格
            hotels_price_restlt = resp.html.xpath('//div[@class="num"]/span/b/text()')

            # 图片
            img_result = resp.html.xpath('//li/a[@target="_blank"]/img/@data-original')
            x = img_result
            y = range(0, len(hotels_result))
            for i,j in zip(x,y):
                print(i)

                if i:
                    img_url = i
                    resp = requests.get(img_url)

                    if not os.path.exists(title):  # 如果data下文件夹不存在city名称的文件夹，则创建city文件夹
                        os.makedirs(title)

                    folder_name = '.\\' + title + '\\{}.jpg'
                    with open(folder_name.format(hotels_result[j]), 'wb') as f:
                        f.write(resp.content)

            return title, city, hotels_result, hotels_price_restlt

        except Exception as e:
            print(traceback.format_exc())

    def save_data(self, data):
        try:
            if not os.path.exists('data'):  # 如果不存在data名称的文件夹，则创建data文件夹
                os.makedirs('data')

            df = pd.DataFrame(data)
            file_name = '.\\data\\' +'data.csv'
            if os.path.exists(file_name):
                df.to_csv(file_name, mode='a', index=False, na_rep='NA',
                          header=False, encoding='gbk')
            else:
                df.to_csv(file_name, mode='a', index=False, na_rep='NA',
                          header=['title', 'city', 'hotels', 'hotels_price'], encoding='gbk')
        except Exception as e:
            print(traceback.format_exc())

    def main(self, url,city):
        try:
            session = HTMLSession()
            resp = session.get(url, headers=headers)
            base_data = self.parser(resp,city)
            data = [base_data]
            self.save_data(data)
        except Exception as e:
            print(traceback.format_exc())


def run():
    city = ['桂林','南宁','梧州','柳州','百色','河池','北海','防城港','贺州','玉林','贵港','钦州','崇左','来宾']
    city_pinyin = ['guilin','nanning','wuzhou','liuzhou','baise','hechi','beihai','fangchenggang','hezhou','yulin','guigang','qinzhou','chongzuo','laibin']
    city_pages = [14, 6, 5, 5, 4, 4, 4, 3, 3, 2, 2, 2, 2, 1]

    q_url = "https://www.cncn.com/piao/"
    h_url = ".htm"

    for k in range(0, len(city)):   #city，爬取city[k]城市中的景点；来宾不爬，只有1页，去掉'/1s'后可爬
        print("===========================景点城市：【"+city[k]+"】===========================")
        for i in range(1, city_pages[k]+1):       #爬取每个城市所有景点，city_pages[k]为该城市存在n页
        # for i in range(1, 2):  # 爬取每个城市所有景点，city_pages[k]为该城市存在n页
            url_first = q_url +city_pinyin[k] +'/1s'+ str(i) + h_url
            html = requests.get(url_first, headers1)
            dom = etree.HTML(html.text)
            h_url_xqy = dom.xpath('//div[@class="list_top"]/a/@href')
            for j in h_url_xqy:
                time.sleep(1)
                url_xqy = "https://www.cncn.com" + j
                print()
                print('景点地址：'+url_xqy)

                # 每个景点的酒店地址
                html_2 = requests.get(url_xqy, headers1)
                dom_2 = etree.HTML(html_2.text)
                url_hotle = dom_2.xpath('//div[@class="media-right"]/div/a/@href')
                str_url_hotle = ''.join(url_hotle)
                print('酒店地址：'+str_url_hotle)

                crawler = Crawler()
                crawler.main(str_url_hotle,city[k])


if __name__ == '__main__':
    start = datetime.datetime.now()
    run()
    end = datetime.datetime.now()
    print('======================================')
    print('Running time: %s Seconds' % (end - start))
