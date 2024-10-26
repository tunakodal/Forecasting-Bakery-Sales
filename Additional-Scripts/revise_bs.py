import pandas as pd

# 1. CSV dosyasını yükleme
sales_3 = pd.read_csv('bakery_sales_3.csv')

# 2. 'datetime' kolonunu silme
if 'datetime' in sales_3.columns:
    sales_3 = sales_3.drop(columns=['datetime'])
    print("'datetime' kolonu silindi.")
else:
    print("'datetime' kolonu bulunamadı, silme işlemi atlandı.")

# 3. Güncellenmiş veriyi 'bakery_sales_4.csv' olarak kaydetme
sales_3.to_csv('bakery_sales_4.csv', index=False)

print("Yeni CSV dosyası 'bakery_sales_4.csv' olarak kaydedildi.")
