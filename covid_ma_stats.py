import requests
from bs4 import BeautifulSoup

URL = "https://www.mass.gov/info-details/covid-19-cases-quarantine-and-monitoring#covid-19-cases-in-massachusetts-"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

for figures in soup.find_all('tr'):
    if figures.td is not None:
        header = figures.th.text
        quantity = figures.td.text
        print(header)
        print(quantity)
