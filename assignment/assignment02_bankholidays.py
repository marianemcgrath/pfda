# Bank Holidays in Northern Ireland
## Author: Mariane McGrath 

# Task: The program should print out the dates of the bank holidays that happen in northern Ireland.

# Import the requests library to get data from a website
import requests

# Get the bank holiday data from specific URL
url = "https://www.gov.uk/bank-holidays.json"

# Use requests to get the data from the URL
response = requests.get(url)

# Convert the data into JSON format 
data = response.json()

# Print the bank holidays in Northern Ireland
# We'll loop through each event, and print date and title
for event in data ["northern-ireland"] ["events"]:
    print (f"{event['title']} on {event ['date']}")

# Source: PFDA3.1 Class Video (5min 02sec)
# Source: https://www.geeksforgeeks.org/python/python-holidays-library/
# Soiurce: https://stackoverflow.com/questions/54987115/uk-bank-holidays-json-read-into-pandas


## Part 2: Write a modified program that print the bank holidays that are unique to Northern Ireland
# (i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or 
# the date of the holiday to decide if it is unique.


# Extract event titles for each region
ni_events = data["northern-ireland"]["events"]
england_events = data["england-and-wales"]["events"]
scotland_events = data["scotland"]["events"]

# We'll create sets of holiday titles for England/Wales and Scotland for fast comparison
england_titles = {event["title"] for event in england_events}
scotland_titles = {event["title"] for event in scotland_events}

# Check each Northern Ireland holiday
for event in ni_events:
    holiday_title = event["title"]

    # Check if the title is NOT found in both England/Wales and Scotland sets
    if holiday_title not in england_titles and holiday_title not in scotland_titles:
        print(f"Exclusive to NI: {holiday_title} on {event['date']}")

print ("Bank holidays unique to Northern Ireland:")

# Source: https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement
# Source: https://www.geeksforgeeks.org/python/python-holidays-library/ 