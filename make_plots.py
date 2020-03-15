import os
os.system('python covid19plot.py -log -dark -deaths -out special_1_deaths US UK IR KR IT')
os.system('python covid19plot.py -log -dark -out special_1_count US UK IR KR IT')

os.system('python covid19plot.py -log -dark -deaths -out middle_europe_deaths FR DE AT IT')
os.system('python covid19plot.py -log -dark -out middle_europe_count FR DE AT IT')

os.system('python covid19plot.py -log -dark -deaths -out north_europe_deaths SE NO DK')
os.system('python covid19plot.py -log -dark -out north_europe_count SE NO DK')