import pandas as pd

# Dosyaları yükleyin
bakery_df = pd.read_csv('bakery_sales_dataset_4.2.csv')
combined_df = pd.read_csv('combined_price_dataset.csv')

# Tarih kolonlarını doğru formatla datetime formatına çevirin
bakery_df['Date'] = pd.to_datetime(bakery_df['Date'], format='%Y-%m-%d')
combined_df['Date'] = pd.to_datetime(combined_df['Date'], format='%y-%m-%d')

# combined_df ile bakery_df'i tarih bazında birleştirin
merged_df = pd.merge(bakery_df, combined_df[['Date', 'Average Price']], on='Date', how='left')

# Eşleşen 'Average Price' değerini 'Avg_Oil_Price' ile güncelleyin
merged_df['Avg_Oil_Price'] = merged_df['Average Price'].combine_first(merged_df['Avg_Oil_Price'])

# Eksik tarihleri bir önceki değerle doldurun
merged_df['Avg_Oil_Price'] = merged_df['Avg_Oil_Price'].ffill()

# Gereksiz 'Average Price' kolonunu kaldırın
merged_df.drop(columns=['Average Price'], inplace=True)

# Sonucu yeni bir dosyaya kaydedin
merged_df.to_csv('bakery_sales_dataset_4.3.csv', index=False)
