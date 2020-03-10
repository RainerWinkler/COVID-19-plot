import os

os.system("python covid19plot.py -log -dark -deaths -out middle_europe_deaths france germany austria italy")
os.system("python covid19plot.py -log -dark -out middle_europe_count france germany austria italy")

os.system("python covid19plot.py -log -dark -deaths -out north_europe_deaths sweden norway denmark")
os.system("python covid19plot.py -log -dark -out north_europe_count sweden norway denmark")