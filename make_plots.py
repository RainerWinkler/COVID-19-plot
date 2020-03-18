import os


os.system('python covid19plot.py -perCapita -log -dark -deaths -out Top_10_deaths -top 1 10 -title "Top 10 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out Top_10_Countries_Cases -top 1 10 -title "Top 10 - Countries with most cases"')
os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_20_deaths -top 11 20 -title "Top 11-20"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_20 -top 11 20 -title "Top 11-20"')
os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_30_deaths -top 21 30 -title "Top 21-30"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_30 -top 21 30 -title "Top 21-30"')
os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_40_deaths -top 31 40 -title "Top 31-40"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_40 -top 31 40 -title "Top 31-40"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out special_1_deaths US UK IR KR IT')
os.system('python covid19plot.py -perCapita -log -dark -out special_1_count US UK IR KR IT')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out middle_europe_deaths FR DE AT IT')
os.system('python covid19plot.py -perCapita -log -dark -out middle_europe_count FR DE AT IT')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out north_europe_deaths SE NO DK')
os.system('python covid19plot.py -perCapita -log -dark -out north_europe_count SE NO DK')