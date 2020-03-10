This is a modified copy of the repository https://github.com/karvla/covid19count

# covid19count
Plots number of confirmed COVID-19 cases for countries worldwide. The data is pulled from 	
[European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases).

You may delete the cache for images in the browser when the plots are not actual.

![example](../../raw/master/middle_europe_count.png)
![example](../../raw/master/middle_europe_deaths.png)

![example](../../raw/master/north_europe_count.png)
![example](../../raw/master/north_europe_deaths.png)

## Usage
Calculate all plots with `python make_plots.py`

To make individual plots about cases use `python covid19plot.py france germany austria`
Country names are in lowercase and have to be like in the read Excel file.
To plot deaths add -deaths for instance `python covid19plot.py -deaths france spain`

To save to file add -out filename for instance `python covid19plot.py france germany austria -out middle_europe_count`
To save to file without displaying a plot add -dark for instance `python covid19plot.py france germany austria -out middle_europe_count -dark`

