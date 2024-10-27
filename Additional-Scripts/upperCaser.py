import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('bakery_sales_4.csv')

# 'Place' sütunundaki 'edinburgh' kelimesini bul ve ilk harfini büyüt
df['Place'] = df['Place'].replace('edinburgh', 'Edinburgh', regex=True)

# Yeni dosyayı kaydet
df.to_csv('bakery_sales_5.csv', index=False)
