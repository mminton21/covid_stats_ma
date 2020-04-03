import requests

URL = "https://www.mass.gov/info-details/covid-19-cases-quarantine-and-monitoring#covid-19-cases-in-massachusetts-"
page = requests.get(URL)
#print(page.content)
