import pandas
from data_scrapping import pull_data

df = pull_data('https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29', 3)

df.columns = range(df.shape[1]) # change the columns index to int 0, 1, 2, 3 ...

df = df[[0,2]]

df = df.iloc[1:11]

# change the columns from the int index to names

df.columns =  ['Country', 'GDP (Milions USD)']

print(df)