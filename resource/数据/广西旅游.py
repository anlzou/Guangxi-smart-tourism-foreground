import requests
from lxml import etree
import time
import pandas as pd


def Spider():
    Scenic_spot_name = []
    Address = []
    Scenic_spot_type = []
    Open_time = []
    Ticket_information = []
    Ticket_price = []
    Introduce = []
    Traffic = []

#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'zh-CN,zh;q=0.9',
#         'cache-control': 'no-cache',
#         # 'cookie':  'UM_distinctid=172b674e5f71cb-034c5dfe424061-3a365305-1fa400-172b674e5f8848; PHPSESSID=4gsduu0v6tmi1lkbsf8cp7kej0; local_zone=320100%7Cnanjing%7C%C4%CF%BE%A9%7C58238; Hm_lvt_d64174522c86449826babe56fb2a88ff=1592199015; CNZZDATA1089612=cnzz_eid%3D725595362-1592200519-https%253A%252F%252Fguilin.cncn.com%252F%26ntime%3D1592200519; Hm_lpvt_d64174522c86449826babe56fb2a88ff=1592203476',
#         'pragma': 'no-cache',
#         # 'referer':  'https://beihai.cncn.com/jingdian/beihai/',
#         'sec-fetch-dest': 'document',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-site',
#         'sec-fetch-user': '?1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#
# }

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    """
    https://guangxi.cncn.com/jingdian/1-1-0-0.html     #最初页面
    https://guangxi.cncn.com/jingdian/1-2-0-0.html

    https://guilin.cncn.com/jingdian/longshengtitian/   #详情页
    https://beihai.cncn.com/jingdian/beihai/

    https://guilin.cncn.com/jingdian/longshengtitian/photo_3702760.htm    #详情页中详情页图片
    https://beihai.cncn.com/jingdian/beihai/photo_4012594.htm

    https://beihai.cncn.com/jingdian/beihai/profile
    """
    # `scenic_spot_name`, `address`, `total_tickets`, `surplus`, `price`, `open_time`, `close_time`, `stars`, `introduce`

    q_url = "https://www.cncn.com/piao/guangxi/1s"
    h_url = ".htm"
    for i in range(1,5):
        url_first = q_url + str(i) + h_url
        #print(url_first)
        html = requests.get(url_first, headers)
        dom = etree.HTML(html.text)
        h_url_xqy = dom.xpath('//div[@class="list_top"]/a/@href')
        for j in h_url_xqy:
            time.sleep(1)
            #构造网址
            url_xqy = "https://www.cncn.com"+j
            #print(url_xqy)
            #获取网页，请求头部
            html_xqy = requests.get(url_xqy, headers)
            dom_xqy = etree.HTML(html_xqy.text)
            #景点名称
            scenic_spot_name = dom_xqy.xpath('//div[@class="title"]/a[1]/h1/text()')
            if scenic_spot_name == []:
                scenic_spot_name.append('None')
            Scenic_spot_name.append(scenic_spot_name)
            print(scenic_spot_name)
            #地址
            address = dom_xqy.xpath('//span[@class="address"]/text()')
            if address == []:
                address.append('None')
            Address.append(address)
            print(address)
            #景点类型
            scenic_spot_type = dom_xqy.xpath('//div[@id="J-MediaLabel"]/a/text()')
            if scenic_spot_type == []:
                scenic_spot_type.append('None')
            Scenic_spot_type.append(scenic_spot_type)
            print(scenic_spot_type)
            #景点开放时间
            open_time = dom_xqy.xpath('//li[@class="time"]/span/text()')
            if open_time == []:
                open_time.append('None')
            Open_time.append(open_time)
            print(open_time)
            #门票信息
            ticket_information = dom_xqy.xpath('//li[@class="promise"]/div/text()')
            if ticket_information == []:
                ticket_information.append('None')
            Ticket_information.append(ticket_information)
            print(ticket_information)
            #门票价格
            ticket_price = dom_xqy.xpath('//div[@class="price-box"]/span/text()')
            if ticket_price == []:
                ticket_price.append('None')
            Ticket_price.append(ticket_price)
            print(ticket_price)
            #详细介绍
            introduce = dom_xqy.xpath('//div[@class="produce_con"]/p/text()')
            if introduce == []:
                introduce.append('None')
            Introduce.append(introduce)
            print(introduce)
            #交通
            traffic = dom_xqy.xpath('//div[@class="produce_con mt20"]/a/@href')
            for i in traffic:
                time.sleep(1)
                html_2_xqy = requests.get(i, headers)
                dom_2_xqy = etree.HTML(html_2_xqy.text)
                traffic = dom_2_xqy.xpath('//div[@class="show_info_con"]/text()')
                if traffic == []:
                    traffic.append('None')
                Traffic.append(traffic)
                print(traffic)

            #图片
            #http://c.cncnimg.cn/037/084/12bb_m.jpg
            h_url_img = dom_xqy.xpath('//ul[@id="tFocus-pic"]/li/a/img/@src')
            for i in h_url_img:
                picture = requests.get('https:{}'.format(i))
                with open(r'G:/travel/picture/{}.jpg'.format(scenic_spot_name),'wb') as f:
                    f.write(picture.content)

    """
    Scenic_spot_name = []
    Address = []
    Scenic_spot_type = []
    Open_time = []
    Ticket_information = []
    Ticket_price = []
    Introduce = []
    Traffic = []
    """
    data = pd.DataFrame()
    data['Scenic_spot_name'] = Scenic_spot_name
    data['Address'] = Address
    data['Scenic_spot_type'] = Scenic_spot_type
    data['Open_time'] = Open_time
    data['Ticket_information'] = Ticket_information
    data['Ticket_price'] = Ticket_price
    data['Introduce'] = Introduce
    data['Traffic'] = Traffic

    data.to_excel('G://travel//scenic_data.xlsx', encoding='utf-8', index=True, index_label='序号')
if __name__ == '__main__':
    Spider()
