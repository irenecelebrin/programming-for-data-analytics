# Task 2: print out the dates of the bank holidays that happen in northern Ireland.
# Author: Irene Celebrin 
# Date: 2025-10-06

# to import data from url
import requests 

# get data from url in json format and transform it into a dictionary. See https://realpython.com/python-requests/ 
holidays = requests.get('https://www.gov.uk/bank-holidays.json').json()

# get list of holidays in northern Ireland 
ni_holidays = holidays['northern-ireland']['events']

# print out the date of each holiday in northern Ireland
print(f"Bank holidays in Northern Ireland (2025-2028):\n")
for holiday in ni_holidays:
    print(f"Holiday: {holiday['title']},\nDate: {holiday['date']}\n")
print("\n")

# EXTRA 
# Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK). 

# Create a list to concatenate the lists of holidays happening across UK constituent countries . See: http://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
uk_holidays = []
for key in holidays.keys():
    if key != 'northern-ireland':
        uk_holidays = uk_holidays + (holidays[key]['events'])

# create a list with all UK holiday dates 
uk_holiday_dates = []
for holiday in uk_holidays: 
    uk_holiday_dates.append(holiday['date'])

# create a list with Northern Ireland holiday dates 
ni_holiday_dates = []
for holiday in ni_holidays:
    ni_holiday_dates.append(holiday['date'])

# Create a list for NI unique holidays 
unique_ni_holidays = []
# verify if each NI holoiday date is not in the UK holiday dates list. See: https://www.geeksforgeeks.org/python/check-if-element-exists-in-list-in-python/
for ni_date in ni_holiday_dates: 
    if ni_date not in uk_holiday_dates:
        unique_ni_holidays.append(ni_date)

# print unique dates 
print(f"Bank holidays unique to Northern Ireland (2025-2028):\n")
for unique_holiday in unique_ni_holidays:
    for holiday in ni_holidays:
        if unique_holiday == holiday['date']:
            print(f"Holiday: {holiday['title']},\nDate: {unique_holiday}\n")