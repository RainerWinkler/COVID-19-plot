This is a modified copy of the repository https://github.com/karvla/covid19count

# covid19count
Plots number of confirmed COVID-19 cases for countries worldwide. The data is pulled from 	
[European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases).

You may delete the cache for images in the browser when the plots are not actual.

##Top 10 cases and death

![example](../../raw/master/top_10.png)
![example](../../raw/master/top_10_deaths.png)

##Top 20 cases and death

![example](../../raw/master/top_20.png)
![example](../../raw/master/top_20_deaths.png)

##Top 30 cases and death

![example](../../raw/master/top_30.png)
![example](../../raw/master/top_30_deaths.png)

##Further examples

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

