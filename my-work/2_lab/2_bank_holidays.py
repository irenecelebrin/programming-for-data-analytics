# Write a program to print json data to the console 
# author: irene celebrin 
# date: 2025-10-06

import pandas as pd 

# set file path 
FILENAME = '2_bank_holidays.json'
FILEPATH = ''
FULLPATH = FILEPATH + FILENAME

'''
# load the data from json file. About pandas read_json: https://www.w3schools.com/python/pandas/pandas_json.asp
df = pd.read_json(FULLPATH)
# print df
print(df)
# print full df 
print(df.to_string())
'''

# import the json data from a url with requests library. see https://reqbin.com/code/python/rituxo3j/python-requests-json-example#:~:text=To%20request%20JSON%20data%20from,JSON%20decoding%20fails%2C%20then%20response. 
import requests 

holidays = requests.get('https://www.gov.uk/bank-holidays.json').json()
#print(holidays)


# the json data is transformed into a dictionary (values are in single quotes vs double quotes in json)

# output only the first holiday in northern ireland 
print(holidays['northern-ireland']['events'][0])
