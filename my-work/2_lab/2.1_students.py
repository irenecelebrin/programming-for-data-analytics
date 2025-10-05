# program to read in the data and output each line as a list. 
# author: irene celebrin 
# date: 2025/10/05

#import csv
import csv 

# set directories 
FILENAME = '2.1_students.csv'
FILEPATH = ''
FULLPATH = FILEPATH + FILENAME

# read the file 
'''
with open(FULLPATH, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
'''

# what is printed? 
# each line is a list. the first line (header) is a list of strings. 
# The other lines are lists of floats (numbers: line n. and age) and strings (names). 
# This is because quoting is non-numeric, which means that non-numeric values are treated as strings, numeric values are treated as floats 


'''
#  Modify the program to deal with the header line separately
with open(FULLPATH, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    line_number = 0
    for line in reader:
        if line_number == 0:
            print(f"{line}\n-------------------")
        else:
            print(line)
        line_number += 1
'''

# Modify the program to calculate the average age, there are a few ways to solve this

import statistics as stats

with open(FULLPATH, 'r') as csvfile:
    # read csv file 
    reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    # avoid line 0, which is header 
    line_number = 0
    # create empty list to store ages
    age = []
    for line in reader:
        # verify header (line 0) is not read 
        if line_number:
            # add age to list 
            age.append(line[1])
        line_number += 1
    # calculate average age
    average_age = round(stats.mean(age),2)
    print(f"The average age of students is {average_age}")


    # instead of using quoting, you can read the age as a number changing the type: age.append(int(line[1])) or float(line[1])

    