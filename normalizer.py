import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. CSV dosyasını yükleyin
df = pd.read_csv('bakery_sales_dataset_4.5.csv')

# 2. Normalizasyon yapmak istediğiniz sütunları seçin
columns_to_normalize = ['isHoliday', 'Brent Price', 'WTI Price', 'Average Price', 'tmin', 'tmax', 'tavg', 'wspd', 'pres',
                        'filter coffee', 'bread', 'croissant', 'angbutter', 'tea', 'cake', 'cookie',
                        'plain bread', 'pastry', 'sandwich', 'hot chocolate', 'orange pound', 'latte',
                        'americano', 'cacao deep', 'wiener', 'pandoro', 'brownie', 'jam', 'farm house bread',
                        'juice', 'muffin', 'scone', 'soup', 'toast', 'scandinavian', 'gateau chocolat',
                        'truffles', 'coke', 'spanish brunch', 'fudge', 'baguette bread', 'tiffin', 'milk tea',
                        'chicken stew', 'jammie dodgers', 'mineral water', 'hearty & seasonal', 'cheesecake',
                        'salad', 'frittata', 'smoothies', 'the nomad', 'vegan mincepie', 'berry ade', 'focaccia']

df_to_normalize = df[columns_to_normalize]

# 3. StandardScaler ile normalizasyon yapın
scaler = StandardScaler()
df_normalized = scaler.fit_transform(df_to_normalize)

# 4. Normalize edilmiş verileri DataFrame'e dönüştürün
df_normalized = pd.DataFrame(df_normalized, columns=columns_to_normalize)

# 5. Normalized verileri orijinal DataFrame'e ekleyin
df[columns_to_normalize] = df_normalized

# 6. Sonuçları yeni bir CSV dosyasına kaydedin
df.to_csv('bakery_sales_dataset_4.5_normalized.csv', index=False)

print("Veriler başarıyla normalleştirildi ve kaydedildi.")