# task 0 - 1
# Write a Jupyter notebook that displays a plot of this projected birth-rates.



import pandas as pd 
import matplotlib.pyplot as plt

# 1. Plot projected birth rates

# Load projected birth to pandas dataframe 
df = pd.read_csv('projectedbirths-cso.csv')

# Set variables 
year = df['Year']
births = df['VALUE']

# plot the data 
fig, ax = plt.subplots()
ax.plot(year, births, marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Projected Births')
ax.set_title('Projected Births in Ireland (2024-2051)')

# Show the plot
plt.show()

