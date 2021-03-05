import json
import pygal
import math

from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique , y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

# 将数据加载到一个列表中
filename = 'btc_close_2017_request.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays =[]
close = []

# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值 (¥)', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

# line_chart_week

# line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
# line_chart.title = '收盘价对数变换 (¥)'
# line_chart.x_labels = dates
# N = 20
# line_chart.x_labels_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('收盘价', close_log)
# line_chart.render_to_file('收盘价对数变换折线图 (¥).svg')
# # 打印每一天的信息
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = int(btc_dict['month'])
#     week = int(btc_dict['week'])
#     weekday = btc_dict['weekday']
#     close = int(float(btc_dict['close']))
#     print("{} is month {} week {}, {}, the close price is {} RMB" .format(date, month, week, weekday, close))