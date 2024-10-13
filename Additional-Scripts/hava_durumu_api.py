import pandas as pd
import requests
from datetime import datetime

# OpenWeatherMap API anahtarınızı buraya girin
api_key = 'REMOVED'

# CSV dosyasını yükleyin
df = pd.read_csv('bakery_sales.csv').head(10)  # Dosya adını uygun şekilde değiştirin

# Hava durumu verilerini depolamak için bir liste oluşturun
weather_data = []

# Her satır için hava durumu verilerini çekin
for index, row in df.iterrows():
    date = row['Date']
    city = row['Place']
    datetime_str = f"{date} 12:00:00"  # Hava durumu verisini almak için saat belirleme
    timestamp = int(datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S').timestamp())

    # API'den hava durumu verilerini çekme
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Hava durumu açıklamasını al
        weather_description = data['weather'][0]['description']
        weather_data.append(weather_description)
    else:
        weather_data.append(None)  # Hava durumu verisi alınamazsa None ekle

# Hava durumu verilerini DataFrame'e ekle
df['Weather'] = weather_data

# Güncellenmiş DataFrame'i yeni bir CSV dosyasına kaydet
df.to_csv('updated_dataset.csv', index=False)
print("Hava durumu verileri başarıyla eklendi ve 'updated_dataset.csv' olarak kaydedildi.")
