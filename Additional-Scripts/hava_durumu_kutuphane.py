from meteostat import Point, Daily
import pandas as pd
import datetime

# Konum belirleme (örnek: İstanbul, Türkiye)
location = Point(41.0082, 28.9784)  # (enlem, boylam)

# Veri aralığı belirleme
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2023, 12, 31)

# Günlük hava durumu verilerini alma
data = Daily(location, start, end)
data = data.fetch()

# Veriyi yazdırma
print(data)
