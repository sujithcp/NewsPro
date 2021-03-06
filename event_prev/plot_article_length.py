
from matplotlib import pyplot as plt
from matplotlib.dates import  date2num
import sqlite3
import datetime as DT

def plotLength():
    connection=sqlite3.connect('../data/news_data.db')
    cursor = connection .cursor()

    data= cursor.execute(''' select date,max(length(news)) as maxlen, min(length(news)) as minlen,avg(length(news)) from News where date>="2016-04-01" group by date''').fetchall()

    data = [i for i in data if i[0] != 'NULL']

    data = [(DT.datetime.strptime(i[0], "%Y-%m-%d"), i[1], i[2],i[3]) for i in data]

    x = [date2num(date) for (date, value1, value2,avg) in data]
    y1 = [value1 for (date, value1, value2, avg) in data]
    y2 = [value2 for (date, value1, value2, avg) in data]
    mean = [avg for (date, value1, value2, avg) in data]

    fig = plt.figure()

    graph = fig.add_subplot(111)

    # Plot the data as a red line with round markers
    graph.plot(x, y1,'ro',x,y2, 'bo', x, mean, 'g-o', linewidth=2)

    # Set the xtick locations to correspond to just the dates you entered.
    graph.set_xticks(x)
    datacopy = []
    n = len(data)
    for i in range(n):
        if i % 14 == 0:
            datacopy.append(data[i][0].strftime("%Y-%m-%d"))
        elif i == n - 1:
            datacopy.append(data[i][0].strftime("%Y-%m-%d"))
        else:
            datacopy.append(" ")
            # Set the xtick labels to correspond to just the dates you entered.

    # graph.set_xticklabels( [date.strftime("%Y-%m-%d") for (date, value) in data])

    graph.set_xticklabels([date for date in datacopy])

    plt.xlabel('Date')
    plt.ylabel('Article Length')
    plt.title('Graph - Date vs Article-Length')
    plt.grid(True)
    plt.ylim(0,30000)
    plt.savefig('Article_len.png')
    plt.show()


plotLength()

