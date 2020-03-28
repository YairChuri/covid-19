import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

#data = pd.read_csv("https://covid.ourworldindata.org/data/full_data.csv")



def plotDate(fId, country, showTotal=False):
    data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")

    # look only at data from Feb-March
    print(country)
    if 'China' == country:
        is_recent = data.loc[:, 'date'].str.contains("2020-(01-(19]|2\d)|02-\d\d|03-(0\d|1[1-5]))")
        #outlier = ~data.loc[:, 'date'].str.contains("2020-02-13")
        data = data[is_recent]
        #data = data[outlier]
    else:
        is_recent = data.loc[:, 'date'].str.contains("\d\d\d\d-0[3]-\d\d")
        data = data[is_recent]


    df = data[data['location'] == country]
    #df['date'] = df['date'].str[5:]

    df.loc[:, 'date'].apply(lambda x: x[5:])

    # data
    timeline = df['date']
    if (showTotal):
        cases = df["total_cases"]
        deaths = df["total_deaths"]
        title = "Total cases and deaths"
    else:
        cases = df["new_cases"]
        deaths = df["new_deaths"]
        title = "New cases and deaths"


    fig = plt.figure(fId)
    ax = fig.add_subplot(1, 1, 1)
    p1 = ax.bar(timeline, cases)
    p2 = ax.bar(timeline, deaths, bottom=cases)
    # ax.plot(israel['date'], israel['total_cases'], 'ro')
    plt.xticks(df['date'], df['date'], rotation='vertical')
    plt.title(country + " - " + date.today().strftime("%d/%m/%Y") + "\n" + title)
    plt.legend((p1[0], p2[0]), ('New cases', 'New deaths'))

showTotal = False

plotDate(1, 'Israel', showTotal)
plotDate(2, 'China', showTotal)
plotDate(3, 'United States', showTotal)
plotDate(4, 'Italy')
plotDate(5, 'Spain')
plotDate(6, 'Sweden')
plotDate(7, 'Japan')
plotDate(8, 'South Korea')
plotDate(9, 'United Kingdom')
plotDate(10, 'World')
plt.show()