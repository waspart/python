import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'D:\\gitrepo\\python\\pythonprogram\\source\\chapter_16\\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    highs = []
    lows = []
    dates = []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)
    # plt.plot(highs, c='red')
    plt.title("Dialy high and low temperatures, - 2014\nDeath Valley", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
