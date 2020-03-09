#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates #Rainer Winkler
from matplotlib.dates import DateFormatter #Rainer Winkler
import xlrd
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime
import numpy as np
import sys

url = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# Changed method to find Excel file URL
xls_url = ""
for link in soup.find_all('a'):
    url2 = link.get('href')
    if type(url2) == str:
        if url2.find(".xls") != -1:
            if xls_url == "":
                xls_url = url2

#xls_link_box = soup.find(text="Download today's data: Geographic distribution of COVID-19 cases worldwide - XLS file")
#xls_url = xls_link_box.parent["href"]


urllib.request.urlretrieve(xls_url, './covid_count.xls')
wb_obj = xlrd.open_workbook('./covid_count.xls') 
xl_sheet = wb_obj.sheet_by_index(0)

date = lambda x: datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(x.value) - 2)
dates = list(map(date, xl_sheet.col(0)[1:]))
countries = list(map(lambda x: x.value.lower(), xl_sheet.col(1)[1:]))
counts = list(map(lambda x: x.value, xl_sheet.col(3)[1:])) # Column 2 cases, Column 3 deaths Rainer Winkler

data = {}
for date, count, country in reversed(list(zip(dates, counts, countries))):
    if country not in data:
        data[country] = {"dates" : [date], "counts" : [count]}
    else:
        data[country]["dates"].append(date)
        data[country]["counts"].append(count)

regions = sys.argv[1:]
regions = sorted(regions, key=lambda r: sum(data[r]["counts"]), reverse=True)

f = plt.figure(figsize=(7,4))
ax = f.add_subplot(111)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")



# See https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/customize-dates-matplotlib-plots-python/ how to format days

ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1)) #Rainer Winkler
date_form = DateFormatter("%m-%d") #Rainer Winkler
ax.xaxis.set_major_formatter(date_form) #Rainer Winkler
#for region in regions:
#    plt.bar(data[region]["dates"], np.cumsum(data[region]["counts"]), alpha=0.6)
for region in regions:
     plt.semilogy(data[region]["dates"], np.cumsum(data[region]["counts"]))

end_date = data[regions[0]]["dates"][-1].date()
plt.legend(regions)
plt.ylabel("Number of confirmed cases")
plt.title("Confirmed deaths per country as of " + str(end_date))
ax.set_xlim([datetime(2020, 2, 15),end_date]) #Rainer Winkler
plt.grid() #Rainer Winkler
plt.savefig("./plotDeath.png") #Rainer Winkler
plt.show()

