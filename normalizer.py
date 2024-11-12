import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. CSV dosyasını yükleyin
df = pd.read_csv('combined_weather_dataset.csv')

# 2. Normalizasyon yapmak istediğiniz sütunları seçin
columns_to_normalize = ['Month', 'Day', 'Year']

df_to_normalize = df[columns_to_normalize]

# 3. StandardScaler ile normalizasyon yapın
scaler = StandardScaler()
df_normalized = scaler.fit_transform(df_to_normalize)

# 4. Normalize edilmiş verileri DataFrame'e dönüştürün
df_normalized = pd.DataFrame(df_normalized, columns=columns_to_normalize)

# 5. Normalized verileri orijinal DataFrame'e ekleyin
df[columns_to_normalize] = df_normalized

# 6. Sonuçları yeni bir CSV dosyasına kaydedin
df.to_csv('combined_weather_dataset_normalized.csv', index=False)

print("Veriler başarıyla normalleştirildi ve kaydedildi.")