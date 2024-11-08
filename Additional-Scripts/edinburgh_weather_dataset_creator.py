from datetime import datetime
from meteostat import Point, Daily
import pandas as pd

# Edinburgh'un koordinatları
edinburgh = Point(55.9533, -3.1883)

# Tarih aralığı: 2010'dan günümüze
start = datetime(2004, 1, 1)
end = datetime.now()

# Günlük hava durumu verilerini al
data = Daily(edinburgh, start, end)
data = data.fetch()

# İlgili sütunları seç
data = data[['tmin', 'tmax', 'tavg', 'wspd', 'pres']]

data = data.dropna()

# Veriyi CSV dosyasına kaydet
data.to_csv('edinburgh_weather_data.csv')

print("Veriler başarıyla çekildi ve 'edinburgh_weather_data.csv' dosyasına kaydedildi.")
