import pandas as pd
from geopy.geocoders import Nominatim
import time

# CSV dosyasını oku
df = pd.read_csv('bakery_sales_5.csv')

# Geolocator nesnesini oluştur
geolocator = Nominatim(user_agent="your_user_agent_name")

# Edinburgh olan ilk 20234 satıra direkt koordinatları ekle
df.loc[:20233, 'Latitude'] = 55.9533456
df.loc[:20233, 'Longitude'] = -3.1883749

# 20234. satırdan sonrasını ayır
korean_cities_df = df.iloc[20234:]

# Unique şehir isimlerini al
unique_cities = korean_cities_df['Place'].unique()

# Her bir unique şehir için koordinat bulma
city_coordinates = {}
for city in unique_cities:
    location = geolocator.geocode(city)
    if location:
        city_coordinates[city] = (location.latitude, location.longitude)
    else:
        city_coordinates[city] = (None, None)
    time.sleep(0.5)  # Bekleme süresini 0.5 saniyeye düşür

# Koordinatları Korean şehirlerine ekle
df.iloc[20234:, df.columns.get_loc('Latitude')] = korean_cities_df['Place'].map(lambda x: city_coordinates[x][0])
df.iloc[20234:, df.columns.get_loc('Longitude')] = korean_cities_df['Place'].map(lambda x: city_coordinates[x][1])

# Güncellenmiş veriyi yeni bir CSV dosyasına kaydet
df.to_csv('bakery_sales_6.csv', index=False)

print("Koordinatlar başarıyla eklendi ve bakery_sales_6.csv dosyası kaydedildi.")
