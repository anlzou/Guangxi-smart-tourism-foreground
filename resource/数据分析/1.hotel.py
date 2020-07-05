f = open("hotel.txt","r",encoding="UTF-8")
lines = f.readlines()
# 每个城市的宾馆个数
my_dict = {}
# 区域的平均价格
price_dict = {}
# 每个城市有多少个区域
city_count_dict = {}

for line in lines:
    line = line.strip()
#    print(line)
    line = line[29:]
    lens = len(line)
    line = line[:lens-2]
#    print("line:"+line)
    splits = line.split("', '")
    # 城市名
    city = splits[1]
    # 价格
    price_list = splits[3].replace("'","").split(", ")
    price_list = price_list[:len(price_list)-6]
    ngbor_all_price = 0
    for price in price_list:
        ngbor_all_price += int(price)
    # 该区域的平均价格
    ngbor_mean_price = ngbor_all_price / len(price_list)
    new_ngbor_mean_price = price_dict.get(city)
    if new_ngbor_mean_price:
        new_ngbor_mean_price = new_ngbor_mean_price + ngbor_mean_price
        price_dict[city] = new_ngbor_mean_price
    else:
        price_dict[city] = ngbor_mean_price

    new_city_count = city_count_dict.get(city)
    if new_city_count:
        city_count_dict[city] = new_city_count+1
    else:
        city_count_dict[city] = 1
    # 宾馆个数
    count = len(splits[2].split(', '))
#    print(city,count)
    new_count = my_dict.get(city)
    if new_count:
        my_dict[city] = new_count + count
    else:
        my_dict[city] = count



# 平均价格
city_list = []
mean_list = []
for k,v in price_dict.items():
    city_list.append(k)
    count = city_count_dict.get(k)
    print(k, v)
    print(count)
    mean_price = v/count
    mean_list.append(mean_price)
print("广西各市景点：",city_list)
print("广西各市景点酒店平均价格：",mean_list)

# 每个城市的宾馆数目
city_list = []
count_list = []
for k,v in my_dict.items():
    city_list.append(k)
    count_list.append(v)
from pyecharts import Bar
# 柱形图
bar = Bar("每个城市的宾馆数", "")
bar.add("宾馆数量", city_list, count_list)
bar.show_config()
bar.render("1.每个城市的宾馆数量.html")

