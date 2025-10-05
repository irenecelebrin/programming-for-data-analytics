# investigate population in Ireland 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cso-populationbyage.csv')

Dublin = df[(df["Administrative Counties"] == "Dublin City Council") |
            (df["Administrative Counties"] == "South Dublin County Council")]

non_Dublin = df[(df["Administrative Counties"] != "Dublin City Council") & 
                 (df["Administrative Counties"] != "South Dublin County Council") &
                 (df["Administrative Counties"] != "Ireland")]

Dublin.insert(5, "Region", "Capital", False)
Dublin = Dublin.drop("Administrative Counties", axis = 1)

print(Dublin.head())
non_Dublin.insert(5, "Region", "non Capital", False)

Dublin_population = Dublin[Dublin['Single Year of Age'] != 'All ages']
non_Dublin_population = df[df['Single Year of Age'] != 'All ages']


fig, ax = plt.subplots(figsize=(20, 5))
ax.scatter(Dublin_population['Single Year of Age'], Dublin_population['VALUE'], color='orange', alpha=0.6, label='Dublin')

plt.show()