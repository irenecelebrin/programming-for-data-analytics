# Task 3: import data from a url (csv) and plot a pie chart 
# Author: Irene Celebrin 

# import required packages 
import pandas as pd
import matplotlib.pyplot as plt

# read csv data from url using pandas: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html 
url = 'https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download' 
data = pd.read_csv(url)

# uncomment to see info on the data in the file 
#print(data.info())

# create array with Emails and modify the data to keep only the domain. 
# how to select subset of dataframe: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html 
# dataframe.replace: https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.replace.html
domains = data['Email'].replace(to_replace='^.+@', value='', regex=True)

# plot the data with matplotlib.pyplot 
counts = domains.value_counts()

# Extract arrays for domains and occurrrences 
# https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html, 
unique_domains = counts.index     
n_domains = counts.values                  

# plot the data in a pie chart. See: https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
fig, ax = plt.subplots()
ax.pie(n_domains, labels = unique_domains)
plt.title('Email domains', loc='left')

# show and save the chart
plt.show()
plt.savefig('piechart')