import pandas as pd

# 'bakery_sales_dataset_full.csv' dosyasını yükle
bakery_sales_full = pd.read_csv('bakery_sales_dataset_full.csv')

# NaN değer içeren satırları sil
bakery_sales_revised = bakery_sales_full.dropna()

# Yeni dosyayı kaydet
bakery_sales_revised.to_csv('bakery_sales_dataset_full_revised.csv', index=False)
