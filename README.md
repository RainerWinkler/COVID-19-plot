This is a modified copy of the repository https://github.com/karvla/covid19count

# covid19count
Plots number of confirmed COVID-19 cases for countries worldwide. The data is pulled from 	
[European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases).

You may delete the cache for images in the browser when the plots are not actual.

## Top 10 cases and death

![example](../../raw/master/Top_10_Countries_Cases.png)
![example](../../raw/master/top_10_deaths.png)

San Marino is not shown (Assumed to be cared for by Italy)
Cases on Diamond Princess are not shown (Singular event)

## Top 11-20 cases and death

![example](../../raw/master/top_20.png)
![example](../../raw/master/top_20_deaths.png)

## Top 21-30 cases and death

![example](../../raw/master/top_30.png)
![example](../../raw/master/top_30_deaths.png)

## Top 31-40 cases and death

![example](../../raw/master/top_40.png)
![example](../../raw/master/top_40_deaths.png)

## Top 41-50 cases and death

![example](../../raw/master/top_50.png)
![example](../../raw/master/top_50_deaths.png)

## Top 51-60 cases and death

![example](../../raw/master/top_60.png)
![example](../../raw/master/top_60_deaths.png)

## Top 61-70 cases and death

![example](../../raw/master/top_70.png)
![example](../../raw/master/top_70_deaths.png)

## Top 71-80 cases and death

![example](../../raw/master/top_80.png)
![example](../../raw/master/top_80_deaths.png)

## Top 81-90 cases and death

![example](../../raw/master/top_90.png)
![example](../../raw/master/top_90_deaths.png)

## Top 91-100 cases and death

![example](../../raw/master/top_100.png)
![example](../../raw/master/top_100_deaths.png)

## Some countries in Asia

![example](../../raw/master/Asia_Cases.png)
![example](../../raw/master/Asia_deaths.png)

## Some countries in Europe

![example](../../raw/master/WestEurope_Cases.png)
![example](../../raw/master/WestEurope_deaths.png)

## Further examples

![example](../../raw/master/special_1_count.png)
![example](../../raw/master/special_1_deaths.png)

![example](../../raw/master/middle_europe_count.png)
![example](../../raw/master/middle_europe_deaths.png)

![example](../../raw/master/north_europe_count.png)
![example](../../raw/master/north_europe_deaths.png)

## Usage
Calculate all plots with `python make_plots.py`

To make individual plots about cases use with the international country codes `python covid19plot.py FR DE AT`
To plot with logarithmic y axis add -log: `python covid19plot.py -log FR DE AT`
Country names are in lowercase and have to be like in the read Excel file.
To plot deaths add -deaths for instance `python covid19plot.py -deaths FR ES`

To use symbols user -format and provide a list of format options: `python covid19plot.py -log AT DE FR -format "ro gs bd" -deaths`
Use the format options from Matlab (As they are used by Matplotlib.

To save to file add -out filename for instance `python covid19plot.py FR DE AT -out middle_europe_count`
To save to file without displaying a plot add -dark for instance `python covid19plot.py FR DE AT -out middle_europe_count -dark`

To display per 100,000 inhabitants add -perCapita

To display tops add -top from to. Countries are ignored. San Marino and Diamond Princes have very many values and are suppressed. Example: `python covid19plot.py -top 1 10`

To set the minimal and maximal values for the y axis use -yFrom <low value> -yTo <high value>: for instance: "-yFrom 1e-2 -yTo 1e3"

