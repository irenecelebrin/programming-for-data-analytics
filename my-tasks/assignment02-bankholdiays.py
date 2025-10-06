# Task 2: print out the dates of the bank holidays that happen in northern Ireland.
# Author: Irene Celebrin 
# Date: 2025-10-06

# to import data from url
import requests 

# get json data from url and transform it into a dictionary. See https://realpython.com/python-requests/ 
holidays = requests.get('https://www.gov.uk/bank-holidays.json').json()

# get list of holidays in northern Ireland 
ni_holidays = holidays['northern-ireland']['events']

# print out the date of each holiday in northern Ireland
print(f"Bank holidays in Northern Ireland:\n")
for holiday in ni_holidays:
    print(holiday['date'])
print("\n")


# Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or the date of the holiday to decide if it is unique.

# store all holidays in the rest of UK in one list. See: http://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
uk_holidays = []
for key in holidays.keys():
    if key != 'northern-ireland':
        uk_holidays = uk_holidays + (holidays[key]['events'])

# create a list with all uk holiday dates 
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
print(f"Bank holidays unique to Northern Ireland:\n")
for unique_holiday in unique_ni_holidays:
    print(unique_holiday)



