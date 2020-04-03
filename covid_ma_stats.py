import requests
from bs4 import BeautifulSoup

URL = "https://www.mass.gov/info-details/covid-19-cases-quarantine-and-monitoring#covid-19-cases-in-massachusetts-"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#results = soup.find_all('div', class_="ma__table--responsive__wrapper")
results = soup.find_all('td')

present_confirmed_ma = results[0]
print(present_confirmed_ma)

total_individuals_quarantine = results[1]
print(total_individuals_quarantine)

total_individuals_complete_quarantine = results[2]
print(total_individuals_complete_quarantine)

total_individuals_current_quarantine = str(results[3])
if len(total_individuals_current_quarantine) == 13:
    ticq = total_individuals_current_quarantine[4:8]
elif len(total_individuals_current_quarantine) == 14:
    ticq = total_individuals_current_quarantine[4:9]
elif len(total_individuals_current_quarantine) == 15:
    ticq = total_individuals_current_quarantine[4:10]

print("The total number of current individuals in quarantine in Massachusetts is " + ticq + ".")
