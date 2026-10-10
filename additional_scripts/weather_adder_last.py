import pandas as pd
from meteostat import Point, Daily
from datetime import datetime

# Veriyi yükleme
df = pd.read_csv('bakery_sales_9.csv')

# Sonuçları tutmak için boş bir DataFrame
weather_data = pd.DataFrame()

# Her satırdaki tarih ve koordinat için hava durumu verilerini çek
for index, row in df.iterrows():
    date = datetime.strptime(row['Date'], '%Y-%m-%d')
    latitude, longitude = row['Latitude'], row['Longitude']

    # Nokta oluşturma (koordinat bazlı)
    location = Point(latitude, longitude)

    # Meteostat'tan günlük hava durumu verisini çekme
    data = Daily(location, date, date)
    data = data.fetch()

    # Eğer veri yoksa atla
    if data.empty:
        continue

    # Tarih ve koordinat bilgisiyle veriyi birleştirme
    data = data.reset_index()  # Tarih indexini normal kolona çevir
    data['Latitude'] = latitude
    data['Longitude'] = longitude

    # Tüm kolonları al ve birleştir
    weather_data = pd.concat([weather_data, data], ignore_index=True)

# Sadece gerekli kolonları seçme
weather_data = weather_data[['time', 'Latitude', 'Longitude', 'tmin', 'tmax', 'tavg', 'wspd', 'pres']]

# Sonuçları CSV olarak kaydetme
weather_data.to_csv('bakery_sales_10.csv', index=False)
print("Hava durumu verileri başarıyla kaydedildi!")
