from __future__ import absolute_import, division, print_function, unicode_literals
from urllib.request import urlopen
import json
import pygal
import math
from itertools import groupby

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

print(len(dates))
line_chart = pygal.Line(show_minor_x_labels=False)
line_chart.x_label_rotation = 20
# line_chart.show
line_chart.title = '收盘价对数变换 （元）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('html.svg')

