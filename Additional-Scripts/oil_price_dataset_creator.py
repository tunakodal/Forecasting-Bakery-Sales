import pandas as pd

# Dosyaları oku
brent_df = pd.read_csv("brent-price-dataset.csv")
wti_df = pd.read_csv("wti-price-dataset.csv")

# Tarihlerden ortak olanları birleştir
merged_df = pd.merge(brent_df[['Date', 'Brent Price']], wti_df[['Date', 'WTI Price']], on='Date', how='inner')

# Ortalama fiyat hesapla
merged_df['Average Price'] = (merged_df['Brent Price'] + merged_df['WTI Price']) / 2

# Sonucu kaydet
merged_df.to_csv("combined_price_dataset.csv", index=False)
