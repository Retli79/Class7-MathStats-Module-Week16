import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)

#read the data
#./dataset/ is a path. Copy and paste the path of the CSV file in your computer to read the data. 
food_consumption = pd.read_csv('food_consumption.csv', index_col=0)
food_consumption.head()
# print(food_consumption.head())



#filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']
# print(be_consumption)

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']
# print(usa_consumption)

# Q-1) Calculate mean and median consumption in Belgium
# belgium_mean = np.mean(be_consumption )
# print(belgium_mean)
# belgium_median = np.median(be_consumption)
# print(belgium_median)

# Q-2) Calculate mean and median consumption of USA
# usa_mean = np.mean(usa_consumption)
# print(usa_mean)
# usa_median = np.median(usa_consumption)
# print(usa_median)


# Work with both countries together
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium' ) | 
                              (food_consumption['country'] == 'USA')]

# print(be_and_usa)
# Q-3) Group by country, select consumption column, and compute mean and median
group_by = be_and_usa.groupby('country')['consumption']
# df_groupby = group_by.agg(['mean', 'median'])
# print(df_groupby)



rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

#Q-4)Plot the histogram of co2_emission for rice
plt.hist(rice_consumption['co2_emission'])
# plt.show()

#Q-5) Calculate mean and median of co2_emission with .agg()
df_agg =rice_consumption['co2_emission'].agg(['mean', 'median'])
# print(df_agg)

#Q-6) Calculate the quintiles of co2_emission

# print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))

#You only need to fill in the missing part.

#Q-7) Calculate the variance and standard deviation of co2_emission 
# for food_categories
df_grouped = food_consumption.groupby('food_category')['co2_emission'].agg(['var', 'std'])
# print(df_grouped)

#Q-8) Create histogram of co2_emission for food_category 'beef'
df_beef = food_consumption[food_consumption['food_category'] == 'beef']['co2_emission']
# print(df_beef)

emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# print(emissions_by_country)

q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country > upper) | (emissions_by_country < lower)]
# print(outliers)

