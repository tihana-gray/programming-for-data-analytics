# program that prints bank holidays in Northern Ireland
# Author: Tihana Gray

import requests

URL = "https://www.gov.uk/bank-holidays.json"

response = requests.get(URL)
data = response.json()

# Data for each region
ni_events = data['northern-ireland']['events']
ew_events = data['england-and-wales']['events']
scot_events = data['scotland']['events']

# Filtering NI holidays to show holidays in 2025
ni_2025 = [event for event in ni_events if event['date'].startswith("2025")]

print("All Northern Ireland Bank Holidays (2025):\n")
for event in ni_2025:
    print(f"{event['date']} - {event['title']}")

# List of other UK holidays in 2025 to avoid duplicates
other_names = {event['title'] for event in ew_events + scot_events if event['date'].startswith("2025")}

print("\nUnique Northern Ireland Bank Holidays (2025):\n")
# Loop through NI holidays and printing only those not in other regions
for event in ni_2025:
    if event['title'] not in other_names:
        print(f"{event['date']} - {event['title']}")
