# Task 0 - 2
# There is also a file with the number of people by age, make a plot that you think is interesting from this data

import pandas as pd
import matplotlib.pyplot as plt


# Load the data 
df = pd.read_csv('cso-populationbyage.csv')

# 1 --- Population by County (latest census year) ---
latest_year = df["CensusYear"].max()
county_data = df[(df["CensusYear"] == latest_year) & 
                 (df["Sex"] == "Both sexes") & 
                 (df["Single Year of Age"] == "All ages") &
                 (df["Administrative Counties"] != "Ireland")]

# Object-oriented style
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(county_data["Administrative Counties"], county_data["VALUE"])
ax.set_title(f"Population by County in {latest_year}")
ax.set_ylabel("Population")
ax.set_xlabel("County")
ax.tick_params(axis="x", rotation=90)

fig.tight_layout()
# plt.show()

# 2 -- Population in Dublin by age 

# population in Dublin by age 
dublin_population = df[(df["Administrative Counties"] == "Dublin City Council") & (df['Single Year of Age'] != 'All ages')]


# plot data 
fig, ax = plt.subplots(figsize=(20, 5))
ax.scatter(dublin_population['Single Year of Age'], dublin_population['VALUE'], color='orange', alpha=0.6)

ax.set_title(f"Population in Dublin by age in {latest_year}")
ax.set_ylabel("Population")
ax.set_xlabel("Age")
ax.tick_params(axis="x", rotation=90)

fig.tight_layout()
#plt.show()


# population in Ireland by age (Dublin-South Dublin vs rest of Ireland)

non_dublin_population = df[(df["Administrative Counties"] != "Dublin City Council") & 
                           (df["Administrative Counties"] != "Ireland") &
                           (df['Single Year of Age'] != 'All ages')]

# plot data 
fig, ax = plt.subplots(figsize=(20, 5))
ax.scatter(dublin_population['Single Year of Age'], dublin_population['VALUE'], color='orange', alpha=0.6)

ax.scatter(non_dublin_population['Single Year of Age'], non_dublin_population['VALUE'], color='green', alpha=0.6)

ax.set_title(f"Population in Dublin vs Ireland by age in {latest_year}")
ax.set_ylabel("Population")
ax.set_xlabel("Age")
ax.tick_params(axis="x", rotation=90)

fig.tight_layout()
plt.show()




# Conclusion: the most populated county in Ireland is by far Dublin, followed by Cork and Fingal. 
# The population in Dublin increases sharply bewetween age 20-30 (Students and young professionals). The it slowly descreases.






