# Bank Holidays in Northern Ireland
## Author: Mariane McGrath 

# Part 1: A program that prints all bank holidays in Northern Ireland

# Import libraries
import requests
import datetime as dt

# Get the bank holiday data from specific URL
url = "https://www.gov.uk/bank-holidays.json"

# Use requests to get the data from the URL
response = requests.get(url)

# Convert the data into JSON format 
data = response.json()


# Print the bank holidays in Northern Ireland
# We'll loop through each event, and print date and title
print("All Northern Ireland Bank Holidays (years 2024 - 2028):")
for event in data["northern-ireland"]["events"]:
    # Convert date from YYYY-MM-DD to DD-MM-YYYY
    dt = event['date'].split('-')
    format_date = f"{dt[2]}-{dt[1]}-{dt[0]}"
    print(f"{format_date}: {event['title']}")

print("\n" + "="*50 + "\n")

## Part 2: A modified program that prints the bank holidays that are unique to Northern Ireland

# First, we'll extract event titles for each region
ni_events = data["northern-ireland"]["events"]
england_events = data["england-and-wales"]["events"]
scotland_events = data["scotland"]["events"]

# Then, we'll create sets of holiday titles for England/Wales and Scotland
england_titles = {event["title"] for event in england_events}
scotland_titles = {event["title"] for event in scotland_events}

# Finally, we'll check each Northern Ireland holiday
# Using a set to track unique titles we've already printed
print_titles = set()

print("Holidays Exclusive to Northern Ireland:")
for event in ni_events:
    holiday_title = event["title"]

    # And we'll make sure that the title is NOT found in England/Wales and Scotland sets
    if holiday_title not in england_titles and holiday_title not in scotland_titles:
        if holiday_title not in print_titles:
            date_parts = event['date'].split('-') # Convert date from YYYY-MM-DD to DD-MM-YYYY
            formatted_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
            print(f"{holiday_title}")
            print_titles.add(holiday_title)
        

# Source: PFDA3.1 Class Video 
# Source: https://www.geeksforgeeks.org/python/python-holidays-library/ (Using holidays library to get bank holidays)
# Source: https://stackoverflow.com/questions/54987115/uk-bank-holidays-json-read-into-pandas (Reading JSON into pandas)
# Source: https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement (Combining for loop and if statement)

