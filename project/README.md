# Programming for data analytics - Project 

This folder includes the final project for the course "Programming for data analytics", Higher Diploma in Science in Data Analytics, ATU Galway Mayo, 2025-2026. 

## Getting started 

### Language and dependencies

Language: Python 3.12
Dependencies: refer to requirements.txt in the root node of the repository. Run the command: 

    pip install requirements.txt

Note: if issues arise when running the notebook, re-install geopandas making sure that all its dependencies are also installed. Use with the command: 

    pip install 'geopandas[all]'


### Structure 


## About this project 

1. Data import and data exploration
2. Data clean-up
3. Analysis: Perceived insecurity among men and women, by state and by municipality
    3.1 Data preparation
    3.2 Plots
    3.3 Analysis
    3.4 Statistics 
4. Analysis: Perceived insecurity by state 
    4.1 Data preparation
    4.2 Perception of insecurity by people aged 18 years and over, by state
        4.2.1 Statistics 
        4.2.2 Plot
        4.2.3 Analysis 
    4.3 Trends in perceived insecurity (2011-2025)
        4.3.1 Statistics
        4.3.2 Plots 
        4.3.3 Analysis 
        4.3.4 Extra: showing polynomial coefficients
    4.4 Perceived insecurity in 2025, by state 
        4.4.1 Plot 
5. Analysis: Reported crime in Mexico 
    5.1 Data preparation
    5.2 Plot
    5.3 Analysis 
6. Correlation between crime and perceived insecurity, 2011-2025
7. Conclusion 
8. Appendix: 
    8.1 A map of Mexico with legend 
    8.2 Line fitting (appendix to 4.3.2)





## Comment 

## References 

pandas: 
columns https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html 
dupes https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html
save to csv https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html 
unique values https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html 



Plots: 

https://matplotlib.org/stable/gallery/color/color_by_yvalue.html 
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
https://matplotlib.org/stable/gallery/color/named_colors.html
x ticks: https://matplotlib.org/stable/gallery/axes_grid1/simple_axisline4.html
subplots: https://www.geeksforgeeks.org/python/how-to-create-subplots-in-seaborn/
ticks https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html 
seaborn ticks https://seaborn.pydata.org/generated/seaborn.FacetGrid.set_xticklabels.html 
seaborn line plot https://seaborn.pydata.org/generated/seaborn.lineplot.html 
suptitle # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html
linestyle: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html 

Maps: 
geopandas: https://geopandas.org/en/stable/getting_started/install.html
map: https://github.com/jschleuss/mexican-states/tree/master?tab=License-1-ov-file
map: https://data.humdata.org/dataset/cod-ab-mex 
code example: https://nbviewer.org/github/pysal/inequality/blob/main/docs/user-guide/viz/pengram.ipynb
getting started with geopandas: https://www.youtube.com/watch?v=aGPQXD-rLgw
