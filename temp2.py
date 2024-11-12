# Correlation Analysis of Items
import pandas as pd


# Veriyi yükleme
df = pd.read_csv('bakery_sales_dataset_4.5.csv')

# `Day` kolonunu silme
df = df.drop(columns=['Day'])

# Ortalama alacak ve toplayacak kolonların listesi
avg_columns = ['isHoliday', 'Brent Price', 'Average Price', 'WTI Price', 'tmax', 'tmin', 'tavg', 'wspd', 'pres']
sum_columns = ['filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie', 'plain bread',
          'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte', 'americano', 'cacao deep',
          'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread', 'juice', 'muffin', 'scone', 'soup',
          'toast', 'scandinavian', 'gateau chocolat', 'truffles', 'coke', 'spanish brunch', 'fudge',
          'baguette bread', 'tiffin', 'milk tea', 'chicken stew', 'jammie dodgers', 'mineral water',
          'hearty & seasonal', 'cheesecake', 'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie',
          'berry ade', 'focaccia']

# Gruplama ve ortalama/toplama işlemi
result = df.groupby(['Year', 'Month']).agg({**{col: 'mean' for col in avg_columns},
                                            **{col: 'sum' for col in sum_columns}}).reset_index()

result.to_csv("temp_3.csv", index=False)