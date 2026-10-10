import pandas as pd

# Dosyaları yükleme
df_cleaned = pd.read_csv('bakery_sales_cleaned_2.1.csv')
df_merged = pd.read_csv('bakery_sales_dataset_3.1.csv')

# 'Day', 'isHoliday', 'Avg_Oil_Price', 'tmin', 'tmax', 'tavg', 'wspd', 'pres' kolonlarını seçme
columns_to_add = ['Day', 'isHoliday', 'Avg_Oil_Price', 'tmin', 'tmax', 'tavg', 'wspd', 'pres']

# Sadece gerekli kolonları al
df_cleaned_filtered = df_cleaned[['Date'] + columns_to_add]

# Merge işlemi: df_merged ve df_cleaned_filtered'ı 'Date' kolonuyla birleştirme
df_final = pd.merge(df_merged, df_cleaned_filtered, on='Date', how='left')

# 'coffee' kolonunun index'ini bulma
coffee_index = df_final.columns.get_loc('coffee')

# Yeni kolonları 'coffee' kolonunun öncesine ekleme
columns_order = list(df_final.columns[:coffee_index]) + columns_to_add + list(df_final.columns[coffee_index:])
df_final = df_final[columns_order]

# Duplicate satırları silme
df_final = df_final.drop_duplicates(subset=['Date'] + [col for col in df_final.columns if col != 'Date'], keep='first')

# Yeni dosyayı kaydetme
df_final.to_csv('bakery_sales_dataset_3.1.csv', index=False)

print("İşlem tamamlandı, yeni dosya 'bakery_sales_dataset_3.1.csv' olarak kaydedildi.")
