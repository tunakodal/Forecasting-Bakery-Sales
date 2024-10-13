import pandas as pd

# CSV formatındaki veriyi yükleyin
df = pd.read_csv('../Forecasting-Bakery-Sales/bakery_sales.csv')

item_counts = df['Items'].value_counts()

# Tüm satırların gösterilmesini sağlıyoruz
pd.set_option('display.max_rows', None)

# Sonucu yazdırıyoruz
print(item_counts)

print("\nToplam ürün sayısı:", len(item_counts))