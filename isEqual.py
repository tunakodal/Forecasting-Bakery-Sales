import pandas as pd

# Dosyayı yükle
df = pd.read_csv("bakery_sales_dataset_4.4.csv")

# Avg_Oil_Price ve Average Price kolonlarını karşılaştır
unequal_rows = df[df['Avg_Oil_Price'] != df['Average Price']]

# Eşit olmayan satırların Date ve Place kolonlarını seç
unequal_rows_info = unequal_rows[['Date', 'Place']]

# Sonuçları yazdır
if not unequal_rows_info.empty:
    print("Eşit olmayan satırların Date ve Place değerleri:")
    print(unequal_rows_info)
else:
    print("Tüm değerler eşittir.")
