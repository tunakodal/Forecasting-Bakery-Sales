import pandas as pd

# 1. CSV dosyalarını yükleme
sales_2 = pd.read_csv('bakery_sales_2.csv')
sales_korea = pd.read_csv('bakery_sales_korea.csv')

# 2. bakery_sales_2'de Date ve Time kolonlarını birleştirip 'datetime' kolonunu oluşturma
sales_2['datetime'] = pd.to_datetime(sales_2['Date'] + ' ' + sales_2['Time'])

# 3. bakery_sales_korea'daki 'datetime' kolonunu datetime tipine çevirme
sales_korea['datetime'] = pd.to_datetime(sales_korea['datetime'])

# 4. Tarih ve saat kolonlarında boş değer olup olmadığını kontrol etme
print(f"sales_2'de boş datetime değerleri: {sales_2['datetime'].isnull().sum()}")
print(f"sales_korea'da boş datetime değerleri: {sales_korea['datetime'].isnull().sum()}")

# 5. İki DataFrame'i 'datetime' kolonuna göre birleştirme (merge)
merged_df = pd.merge(
    sales_2, sales_korea[['datetime', 'place']],
    on='datetime', how='left'
)

# 6. 'Place' kolonunu güncelleme (eşleşen satırlar için)
merged_df['Place'] = merged_df['place'].combine_first(merged_df['Place'])

# 7. Gereksiz kolonları kaldırma
merged_df = merged_df.drop(columns=['place'])

# 8. Güncellenmiş veriyi yeni bir CSV dosyasına kaydetme
merged_df.to_csv('bakery_sales_3.csv', index=False)

print("Güncellenmiş CSV dosyası 'bakery_sales_3.csv' olarak kaydedildi.")
