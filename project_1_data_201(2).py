# -*- coding: utf-8 -*-
"""Project_1_DATA_201.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Q6F2jd1oBcWYMMuHqoy52cX0AeOhGcz
"""

# Emma Poch, DATA201, Spring 2025

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data is sourced from the CORGIS dataset project and was created in 2021
# https://corgis-edu.github.io/corgis/csv/wind_turbines/

# General question: how does the size of a given turbine/a field of turbines correspond with its energy generation efficiency?
# Generation capacity measured in KW; project capacity measured in MW

wind = pd.read_csv('wind_turbines.csv')
wind.head()

wind['Avg_Capacity'] = (wind['Project.Capacity']/wind['Project.Number_Turbines'])*1000

# Visualizations and EDA

plt.scatter('Project.Capacity', 'Avg_Capacity', data = wind, alpha = 0.2)
plt.xlabel('Total Project Capacity (MW)')
plt.ylabel('Average Capacity Per Turbine (KW)')
plt.ylim(0, 7000)
plt.xlim(0, 600)
plt.show

plt.hist('Site.State', data = wind)
plt.xticks(rotation = 90)
plt.show

# Bootstrap sample

len(wind['Turbine.Capacity'])
# 63961 rows in the dataset, so 10% of that would be 6396.

turbines = np.random.choice(wind['Turbine.Capacity'], size=63961)

meds = []
for i in range(1000):
  sample = np.random.choice(turbines)
  samplemeds = meds.append(np.median(sample))
print(np.mean(meds))

conf = np.percentile(meds, [2.5, 97.5])
print(conf)

plt.hist(meds)
for value in conf:
  plt.axvline(value, color='red')