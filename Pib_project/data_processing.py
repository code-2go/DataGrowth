import pandas as pd
import numpy as np
from data_scrapping import pull_data

save_path = r'C:\Users\b_gur\Documents\DataGrowth\Pib_project\top10_worldpib.csv'

df = pull_data('https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29', 3)

# change the columns index to int 0, 1, 2, 3 ...
df.columns = range(df.shape[1]) 

# select the first two columns for the dataframe
df = df[[0,2]] 

# select the top 10 rows
df = df.iloc[1:11] 

# change the columns from the int index to names
df.columns =  ['Country', 'GDP (Million USD)']

# change the data type of the price column from str to int
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# convert the value in million to billion
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']]/1000, 2)

# change the column name from Million to Billion
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'}, inplace=True)

# save the dataframe in csv file
df.to_csv(save_path)