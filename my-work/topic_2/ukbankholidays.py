# program that prints JSON data of UK bank holidays
# Author: Tihana Gray

import requests
url =" https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
#print(data)
# Looks like JSON when printed, but the object in memory is a Python dictionary (dict).

print(data['northern-ireland']['events'][0])