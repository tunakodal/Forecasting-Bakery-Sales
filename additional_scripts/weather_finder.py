import pandas as pd
from meteostat import Point, Daily
from datetime import datetime

# Veriyi yükleme
df = pd.read_csv('updated_with_coordinates.csv')

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

    # Tarih ve koordinat bilgisiyle veriyi birleştirme
    data = data.reset_index()  # Tarih indexini normal kolona çevir
    data['Latitude'] = latitude
    data['Longitude'] = longitude

    # Sonucu ekleme
    weather_data = pd.concat([weather_data, data])

# Sonuçları CSV olarak kaydetme
weather_data.to_csv('weather_with_coordinates.csv', index=False)
print("Hava durumu verileri başarıyla kaydedildi!")
