# https://www.kaggle.com/datasets/datajmcn/residential-property-prices-2020
import pandas as pd
pd.set_option('display.max_rows', 999)
df = pd.read_csv('PPR-2020.csv', encoding="latin-1")


Kerry = df['County'] = 'Kerry'
print(Kerry)
