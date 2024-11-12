import pandas as pd

# CSV dosyasını yükle
df = pd.read_csv('bakery_sales_dataset_4.5.csv')

# Date kolonunu Year, Month, Day olarak ayırma
df['Date'] = pd.to_datetime(df['Date'])  # Tarih formatına dönüştür
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Yeni dataframe'i kontrol et ve kaydet
df.drop(columns=['Date'], inplace=True)  # İsterseniz Date kolonunu kaldırabilirsiniz
df.to_csv('bakery_sales_dataset_4.5.csv', index=False)
