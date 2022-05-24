#https://www.kaggle.com/datasets/datajmcn/residential-property-prices-2020
import pandas as pd
df = pd.read_csv('PPR-2020.csv', encoding="latin-1")

# Preview the data
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.describe(include='all'))
# Review columns and rename to remove the spaces
print(df.columns) # columns before adjustment
df.columns = df.columns.str.replace(' ', '_') # changing the spaces into underscores
print(df.columns) # columns after adjustment

 