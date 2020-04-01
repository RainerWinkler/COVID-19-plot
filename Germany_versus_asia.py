import os

os.system('python covid19plot.py -perCapita -log -dark -deaths -out Germany_Asia_deaths -yFrom 1e-3 -yTo 1 -title "Germany Asia deaths" CN KR JP TW TH VN KH SG MN DE')
os.system('python covid19plot.py -perCapita -log -dark  -out Germany_Asia_Cases -yFrom 1e-3 -yTo 100 -title "Germany Asia cases" CN KR JP TW TH VN KH SG MN DE')
os.system('python covid19plot.py -perCapita  -dark -deaths -out Germany_Asia_lin_deaths -yFrom 0 -yTo 1 -title "Germany Asia deaths" CN KR JP TW TH VN KH SG MN DE')
os.system('python covid19plot.py -perCapita  -dark  -out Germany_Asia_lin_Cases -yFrom 0 -yTo 100 -title "Germany Asia cases" CN KR JP TW TH VN KH SG MN DE')
