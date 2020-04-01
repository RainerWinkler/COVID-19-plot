import os

os.system('python covid19plot.py -perCapita -log -dark -deaths -out Asia_deaths -yFrom 1e-3 -yTo 1e2 -title "Asia deaths" CN KR JP TW TH VN KH SG MN')
os.system('python covid19plot.py -perCapita -log -dark  -out Asia_Cases -yFrom 1e-3 -yTo 1e3 -title "Asia cases" CN KR JP TW TH VN KH SG MN')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out WestEurope_deaths -yFrom 1e-3 -yTo 1e2 -title "Europe deaths" IE UK NO SE FI DK NL BE DE CH AT ES FR IT')
os.system('python covid19plot.py -perCapita -log -dark  -out WestEurope_Cases -yFrom 1e-3 -yTo 1e3 -title "Europe cases" IE UK NO SE FI DK NL BE DE CH AT ES FR IT')


os.system('python covid19plot.py -perCapita -dark -deaths -out Asia_deaths_lin -yFrom 0 -yTo 25 -title "Asia deaths" CN KR JP TW TH VN KH SG MN')
os.system('python covid19plot.py -perCapita -dark  -out Asia_Cases_lin -yFrom 0 -yTo 250 -title "Asia cases" CN KR JP TW TH VN KH SG MN')

os.system('python covid19plot.py -perCapita -dark -deaths -out WestEurope_deaths_lin -yFrom 0 -yTo 25 -title "Europe deaths" IE UK NO SE FI DK NL BE DE CH AT ES FR IT')
os.system('python covid19plot.py -perCapita -dark  -out WestEurope_Cases_lin -yFrom 0 -yTo 250 -title "Europe cases" IE UK NO SE FI DK NL BE DE CH AT ES FR IT')



os.system('python covid19plot.py -perCapita -log -dark -deaths -out Top_10_deaths -top 1 10 -yFrom 1e-3 -yTo 1e2 -title "Top 10 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out Top_10_Countries_Cases -top 1 10 -yFrom 1e-3 -yTo 1e3 -title "Top 10 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_20_deaths -top 11 20 -yFrom 1e-3 -yTo 1e2 -title "Top 11-20 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_20 -top 11 20 -yFrom 1e-3 -yTo 1e3 -title "Top 11-20 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_30_deaths -top 21 30 -yFrom 1e-3 -yTo 1e2 -title "Top 21-30 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_30 -top 21 30 -yFrom 1e-3 -yTo 1e3 -title "Top 21-30 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_40_deaths -top 31 40 -yFrom 1e-3 -yTo 1e2 -title "Top 31-40 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_40 -top 31 40 -yFrom 1e-3 -yTo 1e3 -title "Top 31-40 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_50_deaths -top 41 50 -yFrom 1e-3 -yTo 1e2 -title "Top 41-50 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_50 -top 41 50 -yFrom 1e-3 -yTo 1e3 -title "Top 41-50 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_60_deaths -top 51 60 -yFrom 1e-3 -yTo 1e2 -title "Top 51-60 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_60 -top 51 60 -yFrom 1e-3 -yTo 1e3 -title "Top 51-60 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_70_deaths -top 61 70 -yFrom 1e-3 -yTo 1e2 -title "Top 61-70 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_70 -top 61 70 -yFrom 1e-3 -yTo 1e3 -title "Top 61-70 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_80_deaths -top 71 80 -yFrom 1e-3 -yTo 1e2 -title "Top 71-80 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_80 -top 71 80 -yFrom 1e-3 -yTo 1e3 -title "Top 71-80 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_90_deaths -top 81 90 -yFrom 1e-3 -yTo 1e2 -title "Top 81-90 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_90 -top 81 90 -yFrom 1e-3 -yTo 1e3 -title "Top 81-90 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out top_100_deaths -top 91 100 -yFrom 1e-3 -yTo 1e2 -title "Top 91-100 - Countries with most deaths"')
os.system('python covid19plot.py -perCapita -log -dark  -out top_100 -top 91 100 -yFrom 1e-3 -yTo 1e3 -title "Top 91-100 - Countries with most cases"')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out special_1_deaths US UK IR KR IT RU')
os.system('python covid19plot.py -perCapita -log -dark -out special_1_count US UK IR KR IT RU')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out middle_europe_deaths FR DE AT IT CZ SK')
os.system('python covid19plot.py -perCapita -log -dark -out middle_europe_count FR DE AT IT CZ SK')

os.system('python covid19plot.py -perCapita -log -dark -deaths -out north_europe_deaths SE NO DK')
os.system('python covid19plot.py -perCapita -log -dark -out north_europe_count SE NO DK')