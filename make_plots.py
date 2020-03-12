import os
os.system('python covid19plot.py -log -dark -deaths -out special_1_deaths "united states of america" "united kingdom" iran "south korea" italy')
os.system('python covid19plot.py -log -dark -out special_1_count "united states of america" "united kingdom" iran "south korea" italy')

os.system('python covid19plot.py -log -dark -deaths -out middle_europe_deaths france germany austria italy')
os.system('python covid19plot.py -log -dark -out middle_europe_count france germany austria italy')

os.system('python covid19plot.py -log -dark -deaths -out north_europe_deaths sweden norway denmark')
os.system('python covid19plot.py -log -dark -out north_europe_count sweden norway denmark')