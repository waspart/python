from __future__ import absolute_import, division, print_function, unicode_literals
from urllib.request import urlopen
import json
import pygal
import math
from itertools import groupby


def draw(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        print("y_list:{}\t".format(y_list))
        xy_map.append([x, sum(y_list)/len(y_list)])

    # print(xy_map)
    x_unique, y_mean = zip(*xy_map)
    # print(x_unique)
    # print(y_mean)
    line_chart = pygal.Line()
    line_chart._title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

path = "D:\\gitrepo\\python\\pythonprogram\\source\\chapter_16\\btc-master (16.2)\\btc_close_2017.json"
with open(path, "r") as f:
    # print(f)
    btc_data = json.load(f)

dates, months, weeks, weekdays, close = [], [], [], [], []
for bit_dict in btc_data:
    dates.append(bit_dict['date'])
    months.append(bit_dict['month'])
    weeks.append(bit_dict['week'])
    weekdays.append(bit_dict['weekday'])
    close.append(float(bit_dict['close']))
    # date = bit_dict['date']
    # month = bit_dict['month']
    # week = bit_dict['week']
    # weekday = bit_dict['weekday']
    # close = float(bit_dict['close'])
    # print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

# print("dates 值为 {}".format(dates))
idx_month = dates.index('2017-12-01')
# print(idx_month)
line_chart_month = draw(months[:idx_month], close[:idx_month], "收盘价月日均值（元）", "月日均值")
line_chart_month


# print(len(dates))
# line_chart = pygal.Line(show_minor_x_labels=False)
# line_chart.x_label_rotation = 20
# # line_chart.show
# line_chart.title = '收盘价对数变换 （元）'
# line_chart.x_labels = dates
# N = 20
# line_chart.x_labels_major = dates[::N]
# close_log = [math.log10(_) for _ in close]
# line_chart.add('log收盘价', close_log)
# line_chart.render_to_file('html.svg')

