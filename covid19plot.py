#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates #Rainer Winkler
from matplotlib.dates import DateFormatter #Rainer Winkler
import xlrd
from bs4 import BeautifulSoup
import requests
import urllib.request
from datetime import datetime
from datetime import timedelta 
import numpy as np
import sys
import csv

# Constants
countryTextColumn = 6 # was 1
casesColumn = 4 # was 2
deathColumn = 5 # was 3
countryIDColumn = 7 # was 4

# Defaults
column = casesColumn # This is the column for cases
column_text = "cases"
regions = [] # The list of regions to 
filename = ""
dark = ""
log = ""
format = ""
perCapita = ""
top = ""
topToSearch = ""
topFromFound = ""
topToFound = ""
supTitle = ""
yFrom = ""
yTo = ""
dataFile = ""
# Evaluate arguments
arguments = sys.argv[1:]
for arg in arguments:
    if ( arg == "-deaths" ) : 
        column = deathColumn # This is the columns for deaths
        column_text = "deaths"
    elif ( arg == "-out" ) :
        filename = "xxx"
    elif ( arg == "-dark" ) :
        dark = "X"
    elif ( arg == "-log" ):
        log = "X"
    elif ( arg == "-format" ):
        format = "xxx"
    elif ( arg == "-perCapita" ):
        perCapita = "X"
    elif ( arg == "-top" ):
        top = "X"
        topToSearch = "X"
    elif ( arg == "-title" ):
        supTitle = "xxx"
    elif ( arg == "-yFrom" ):
        yFrom = "xxx"
    elif ( arg == "-yTo" ):
        yTo = "xxx"
    elif ( arg == "-dataFile" ):
        dataFile = "xxx"
    else:
        if filename == "xxx":
            filename = arg
        elif dataFile == "xxx":
            dataFile = arg
        elif supTitle == "xxx":
            supTitle = arg
        elif format == "xxx":
            format = arg
            formats = format.split() # Split at white space
        elif topToSearch == "X":
            if topFromFound == "":
                topFrom = int(arg)
                topFromFound = "X"
            elif topFromFound == "X":
                topTo = int(arg)
                topToFound = "X"
                topToSearch = ""
        elif yFrom == "xxx":
            yFrom = arg
        elif yTo == "xxx":
            yTo = arg
        else:
            regions.append(arg)


#url = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"

if dataFile == "" :
    
    url = "https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide"
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
# Changed method to find Excel file URL
    xls_url = ""
    for link in soup.find_all('a'):
        url2 = link.get('href')
        #print(url2)
        if type(url2) == str:
            position = url2.find(".xls")
            #print(str(position))
            if url2.find(".xls") != -1:
                if xls_url == "":
                    xls_url = url2
                    #print("found" + xls_url)
    #print(xls_url)
    #xls_link_box = soup.find(text="Download today's data: Geographic distribution of COVID-19 cases worldwide - XLS file")
    #xls_link_box = soup.find(text="ct__link")
    #xls_url = xls_link_box.parent["href"]
    dataFile = 'covid_count.xls'

    urllib.request.urlretrieve(xls_url, './' + dataFile)


wb_obj = xlrd.open_workbook('./' + dataFile) 
xl_sheet = wb_obj.sheet_by_index(0)

population = dict()
countryText = dict()
allRegions = []
with open('CountriesPopulation.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        population[row[1]] = row[2]
        countryText[row[1]] = row[0]

date = lambda x: datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(x.value) - 2)
dates = list(map(date, xl_sheet.col(0)[1:]))
countries = list(map(lambda x: x.value, xl_sheet.col(countryIDColumn)[1:])) # Column with Country Code
counts = list(map(lambda x: x.value, xl_sheet.col(column)[1:])) # Column 2 cases, Column 3 deaths Rainer Winkler

#countries = list(xl_sheet.col(4)[1:], xl_sheet.col(1)[1:])
#counts = list(xl_sheet.col(4)[1:], xl_sheet.col(column)[1:]) # Column 2 cases, Column 3 deaths Rainer Winkler

data = {}
for date, count, country in reversed(list(zip(dates, counts, countries))):
    if country not in data:
        if perCapita == "":
            data[country] = {"dates" : [date], "counts" : [count]}
        else:
            perCapitaValue = 0.
            if count != "":
                perCapitaValue = int(count) * 100000/float(population[country]) # First time case per country is calculated
            data[country] = {"dates" : [date], "counts" : [perCapitaValue]}
    else:
        data[country]["dates"].append(date)
        dummy = 0
        if country == 'JPG11668':
            #Ignore Cruise Ship
            dummy = 1
        elif country == 'SM':
            #Ignore San Marino, assume it to be cared for by Italy
            dummy = 2
        elif country == 'VA':
            #Ignore Holy See, assume it to be cared for by Italy
            dummy = 3
        else:
            allRegions.append(country)
        if perCapita == "":
            data[country]["counts"].append(count)
        else:
            data[country]["counts"].append(count*100000/float(population[country])) # Second time case per country is calculated

# Remove duplicates
allRegions = list( dict.fromkeys(allRegions) )
            
if top == "X":
    regions = allRegions

# Sort by last value descending. This helps people with restricted color vision to associate the legend to the lines
regions = sorted(regions, key=lambda r: sum(data[r]["counts"]), reverse=True)
if top == "X":
    regions = regions[topFrom-1:topTo-1]

f = plt.figure(figsize=(6.4*1.5,4.8*1.5))
ax = f.add_subplot(111)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")



# See https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/customize-dates-matplotlib-plots-python/ how to format days

ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1)) #Rainer Winkler
date_form = DateFormatter("%m-%d") #Rainer Winkler
ax.xaxis.set_major_formatter(date_form) #Rainer Winkler
#for region in regions:
#    plt.bar(data[region]["dates"], np.cumsum(data[region]["counts"]), alpha=0.6)
index = 0
legendText = []
for region in regions:
     #plt.semilogy(data[region]["dates"], np.cumsum(data[region]["counts"]))
     legendText.append( countryText[region] );
     if format != "":
         plt.plot(data[region]["dates"], np.cumsum(data[region]["counts"]), formats[index])
     else:
         plt.plot(data[region]["dates"], np.cumsum(data[region]["counts"]))
     index = index + 1
if log == "X":
    plt.yscale("log")
end_date = data[regions[0]]["dates"][-1].date()
end_date_plot = end_date + timedelta(days=1)
plt.legend(legendText)
if perCapita == "":
    plt.ylabel("Number of confirmed " + column_text)
else:
    plt.ylabel("Number of confirmed " + column_text + " per 100,000 inhabitants" )
if perCapita == "":
    plt.title("Confirmed " + column_text + " per country as of " + str(end_date))
    if supTitle != "":
        plt.suptitle(supTitle)
else:
    plt.title("Confirmed " + column_text + " per country per 100,000 inhabitants as of " + str(end_date))
    if supTitle != "":
        plt.suptitle(supTitle)
ax.set_xlim([datetime(2020, 2, 15),end_date_plot]) #Rainer Winkler
if yFrom != "":
    ax.set_ylim(float(yFrom),float(yTo))
plt.grid() #Rainer Winkler
if filename != "" :
    plt.savefig("./" + filename + ".png") #Rainer Winkler
if dark == "" :
    plt.show()

