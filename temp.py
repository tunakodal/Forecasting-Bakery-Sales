import pandas as pd
import numpy as np

# Dosyayı yükle
df = pd.read_csv('bakery_sales_dataset_4.2.csv')

# Avg_Oil_Price sütunundaki 58.94499969482422 değerlerini NaN olarak değiştir
df['Avg_Oil_Price'] = df['Avg_Oil_Price'].replace(58.94499969482422, np.nan)

# Dosyayı üzerine kaydet
df.to_csv('bakery_sales_dataset_4.2.csv', index=False)
