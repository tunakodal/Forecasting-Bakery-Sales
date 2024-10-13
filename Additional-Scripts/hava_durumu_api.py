from datetime import datetime
from meteostat import Point, Daily

# Konumun belirlenmesi: Enlem, Boylam, Yükseklik
location = Point(41.015137, 28.979530, 50)  # İstanbul koordinatları örnek olarak kullanıldı

# Tarih aralığı
start = datetime(2023, 9, 1)
end = datetime(2023, 9, 26)

# Günlük hava durumu verilerini çek
data = Daily(location, start, end)
data = data.fetch()

# Çıktıyı ekrana yazdır
print(data)
