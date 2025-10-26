# Lab 4, exercise 3: 
# Find regular expressions in 4_smaller_access.log

import re

smaller_log = '4_smaller_access.log'
regex = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# find IP address 
'''
with open (smaller_log) as input_file: 
    for line in input_file:
        foundtextlist = re.findall(regex, line)
        if (len(foundtextlist) != 0):
            print(foundtextlist)
'''
regex2 = ":[0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}"

# remove seconds from hour and copy to new file 

smaller_log_new = 'smaller_log.new.txt'
with open (smaller_log) as input_file: 
    with open (smaller_log_new, 'w') as file: 
        for line in input_file: 
            new_line = re.sub(regex2, '', line)
            file.write(new_line)
