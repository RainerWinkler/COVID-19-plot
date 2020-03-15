import os
os.system('python covid19plot.py -log -dark -deaths -out special_1_deaths "United States of America" "United Kingdom" Iran "South Korea" Italy')
os.system('python covid19plot.py -log -dark -out special_1_count "United States of America" "United Kingdom" Iran "South Korea" Italy')

os.system('python covid19plot.py -log -dark -deaths -out middle_europe_deaths France Germany Austria Italy')
os.system('python covid19plot.py -log -dark -out middle_europe_count France Germany Austria Italy')

os.system('python covid19plot.py -log -dark -deaths -out north_europe_deaths Sweden Norway Denmark')
os.system('python covid19plot.py -log -dark -out north_europe_count Sweden Norway Denmark')