import matplotlib.pyplot as plt
import requests
import numpy as np

def get_bar(data, label, title, color):
    n_groups = 477
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.1
    opacity = 0.3
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, data, bar_width,
                     alpha=opacity,
                     color=color,
                     error_kw=error_config,
                     label=label)

    plt.xlabel('Days')
    plt.ylabel('Stock Value')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

def get_legend(data, label):
    fig, ax = plt.subplots()
    ax.plot(open_vals, 'k--', label='Open')
    ax.plot(close_vals, 'k:', label='Close')
    ax.plot(data, 'k', label=label)

    legend = ax.legend(loc='upper center', shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(1.5)

    plt.show()


# use Quandl's api to get information about Facebook's stocks
request = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/FB.json?end_date=2014-04-11?api_key=w4mFn8DZ_okL3s1zM6Dm').json()
data = request['dataset']['data']
dates = []
open_vals = []
high_vals = []
low_vals = []
close_vals = []

# init stock values
for day in data:
    dates.append(day[0])
    open_vals.append(day[1])
    high_vals.append(day[2])
    low_vals.append(day[3])
    close_vals.append(day[4])

# generate graphs
get_bar(low_vals, 'Low', 'Low Stock Values over the Last Year and a Half', 'r')
get_bar(high_vals, 'High', 'High Stock Values over the Last Year and a Half', 'b')
get_bar(open_vals, 'Open', 'Open Stock Values over the Last Year and a Half', 'g')
get_bar(close_vals, 'Close', 'Close Stock Values over the Last Year and a Half', 'y')

get_legend(high_vals, 'High')
get_legend(low_vals, 'Low')



