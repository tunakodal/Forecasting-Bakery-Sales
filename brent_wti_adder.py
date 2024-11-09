import pandas as pd

# Dosyaları yükle
bakery_df = pd.read_csv("bakery_sales_dataset_4.3.csv")
price_df = pd.read_csv("combined_price_dataset.csv")

# Date kolonlarını tarih formatına dönüştür
bakery_df['Date'] = pd.to_datetime(bakery_df['Date'], format="%Y-%m-%d")
price_df['Date'] = pd.to_datetime(price_df['Date'], format="%y-%m-%d")


# İki dosyayı Date kolonuna göre birleştir
merged_df = pd.merge(bakery_df, price_df, on="Date", how="left")

# Eksik değerleri bir önceki geçerli değerle doldur (forward fill)
merged_df.ffill(inplace=True)

# Sonuçları yeni bir CSV dosyasına kaydet
merged_df.to_csv("bakery_sales_dataset_4.4.csv", index=False)
