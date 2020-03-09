import os

os.system("python covid19plot.py -dark -deaths -out middle_europe_deaths france germany austria")
os.system("python covid19plot.py -dark -out middle_europe_count france germany austria")

os.system("python covid19plot.py -dark -deaths -out north_europe_deaths sweden norway denmark")
os.system("python covid19plot.py -dark -out north_europe_count sweden norway denmark")