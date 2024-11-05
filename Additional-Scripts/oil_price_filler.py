import pandas as pd

# Dosyayı yükleyin
df = pd.read_csv('oil_prices_doc.csv')

# 'Date' sütununu datetime olarak ayarla
df['Date'] = pd.to_datetime(df['Date'])

# Tüm tarih aralığını oluştur (ilk ve son tarih arasında)
full_date_range = pd.date_range(start=df['Date'].min(), end=df['Date'].max(), freq='D')

# Tarih sütununu bu aralıkla yeniden endeksle ve eksik tarihleri doldur
df = df.set_index('Date').reindex(full_date_range).rename_axis('Date').reset_index()

# Eksik değerleri bir önceki dolu değerle doldur
df = df.ffill()

# Güncellenmiş dosyayı kaydedin
df.to_csv('oil_prices_doc_filled.csv', index=False)
