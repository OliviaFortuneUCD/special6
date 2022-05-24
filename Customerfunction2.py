import pandas as pd
pd.set_option('display.max_rows', 999)
df = pd.read_csv('PPR-2020.csv', encoding="latin-1")


# Get rid of $ and , in the SAL-RATE, then convert it to a float
def money_to_float(money_str):
    return float(money_str.replace("$","").replace(",",""))

df['Price'].apply(money_to_float)