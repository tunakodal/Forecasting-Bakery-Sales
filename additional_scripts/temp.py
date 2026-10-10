import pandas as pd

# Dosyayı yükleyin
df = pd.read_csv('bakery_sales_dataset_full.csv')

# NaN değerleri içeren satırları kaldırın
df_cleaned = df.dropna()

# Sonucu yeni bir dosyaya kaydedin
df_cleaned.to_csv('temp.csv', index=False)

print("NaN değerleri kaldırıldı ve 'temp.csv' dosyası oluşturuldu.")
