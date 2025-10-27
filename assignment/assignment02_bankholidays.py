# The program should print out the dates of the bank holidays that happen in northern Ireland.

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

for event in data ["northern-ireland"] ["events"]:
    print (f"{event['title']} on {event ['date']}")

# Source: PFDA3.1 Class Video (5min 02sec)
# Source: https://www.geeksforgeeks.org/python/python-holidays-library/


# Modified program that print the bank holidays that are unique to Northern Ireland
# (i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or 
# the date of the holiday to decide if it is unique.

