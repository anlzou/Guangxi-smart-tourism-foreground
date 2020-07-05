f = open("spot.txt","r",encoding="UTF-8")
lines = f.readlines()

spolt_count_dict = {}
xing_count_dict = {}
for line in lines:
    line = line.strip()
    # print(line)
    splits =line.split("', '")
    # 城市
    city = splits[2]
    count = spolt_count_dict.get(city)
    if count:
        spolt_count_dict[city] = count+1
    else:
        spolt_count_dict[city] = 1
    # 星级个数
    xing = splits[len(splits)-1].split("'")[0]
    count = xing_count_dict.get(xing)
    if count:
        xing_count_dict[xing] = count+1
    else:
        xing_count_dict[xing] = 1
# 每个城市的景点个数 - 折线图
spot_city = []
spot_count = []
for k,v in spolt_count_dict.items():
    print(k,v)
    spot_city.append(k)
    spot_count.append(v)
from pyecharts import Line
line = Line("每个城市的景点个数","")
# is_label_show是设置上方数据是否显示
line.add("景点个数", spot_city, spot_count, is_label_show=True)
line.render("2.每个城市的景点个数.html")

# 每个星级的所占的比例
xing_name = []
xing_count = []
for k,v in xing_count_dict.items():
    x_name = ""
    if k == "2":
        x_name = "2星级"
    elif k == "3":
        x_name = "3星级"
    elif k == "4":
        x_name = "4星级"
    elif k == "5":
        x_name = "5星级"
    xing_name.append(x_name)
    xing_count.append(v)

from pyecharts import Pie
# 设置主标题与副标题，标题设置居中，设置宽度为900
pie = Pie("每个星级级别的景点数目", "",title_pos='right',width=900)
# 加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
pie.add("蒸发量", xing_name, xing_count ,center=[75,50],is_legend_show=True,is_label_show=True)
# 保存图表
pie.render("3.每个星级级别的景点数目.html")