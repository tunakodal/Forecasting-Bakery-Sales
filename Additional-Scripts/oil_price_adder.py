import pandas as pd

# Dosyaları yükleyin
bakery_sales = pd.read_csv('bakery_sales_7.csv')
oil_prices = pd.read_csv('oil_prices_doc_filled.csv')

# 'Date' sütunlarını datetime formatına çevirin ve UTC zaman dilimine göre ayarlayın
bakery_sales['Date'] = pd.to_datetime(bakery_sales['Date']).dt.tz_localize('UTC')
oil_prices['Date'] = pd.to_datetime(oil_prices['Date']).dt.tz_localize('UTC')

# Zaman dilimini kaldırarak sadece tarihleri karşılaştırmak için
bakery_sales['Date'] = bakery_sales['Date'].dt.tz_localize(None)
oil_prices['Date'] = oil_prices['Date'].dt.tz_localize(None)

# İki DataFrame'i 'Date' sütununa göre birleştirin
merged_df = pd.merge(bakery_sales, oil_prices, on='Date', how='left')

# Sonuçları yeni bir CSV dosyasına kaydedin
merged_df.to_csv('bakery_sales_8.csv', index=False)
