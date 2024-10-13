import numpy as np
import pandas as pd
from meteostat import Point, Daily
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import datetime
"""
15-16 civarında olmalıydı
2024-10-14: Tahmin Edilen Ortalama Sıcaklık: 19.34 °C
2024-10-15: Tahmin Edilen Ortalama Sıcaklık: 19.37 °C
2024-10-16: Tahmin Edilen Ortalama Sıcaklık: 19.39 °C
2024-10-17: Tahmin Edilen Ortalama Sıcaklık: 19.42 °C
2024-10-18: Tahmin Edilen Ortalama Sıcaklık: 19.45 °C
2024-10-19: Tahmin Edilen Ortalama Sıcaklık: 19.47 °C
2024-10-20: Tahmin Edilen Ortalama Sıcaklık: 19.50 °C
"""

# Konum belirleme (örnek: İstanbul, Türkiye)
location = Point(41.0082, 28.9784)

# Veri aralığı belirleme
start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2024, 10, 13)

# Günlük hava durumu verilerini alma
data = Daily(location, start, end)
data = data.fetch()

# Veriyi hazırlama
data.reset_index(inplace=True)
data['date'] = data['time'].dt.date
data['day_of_year'] = data['time'].dt.dayofyear

# Özellikler ve hedef değişkeni belirleme
X = data[['day_of_year']]
y = data['tavg']  # Ortalama sıcaklık

# Eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model oluşturma
model = LinearRegression()
model.fit(X_train, y_train)

# Bugünün tarihini alma ve yarından itibaren 7 gün için tahmin yapma
today = datetime.date.today()
days_ahead = np.arange(1, 8).astype(int)  # Yarından itibaren 7 gün

# Gelecek günleri hesaplama
future_days = [today + datetime.timedelta(days=int(i)) for i in days_ahead]
future_day_of_year = [d.timetuple().tm_yday for d in future_days]

# Tahmin yapma
X_future = pd.DataFrame(future_day_of_year, columns=['day_of_year'])
future_predictions = model.predict(X_future)

# Sonuçları yazdırma
for i, (day, pred) in enumerate(zip(future_days, future_predictions)):
    print(f"{day}: Tahmin Edilen Ortalama Sıcaklık: {pred:.2f} °C")

# Tahminleri görselleştirme
plt.figure(figsize=(10, 6))
plt.scatter(X['day_of_year'], y, color='blue', label='Gerçek Değerler')
plt.scatter(future_day_of_year, future_predictions, color='red', label='Tahmin Edilen Değerler', marker='x')
plt.title('Sıcaklık Tahmini')
plt.xlabel('Yılın Günü')
plt.ylabel('Ortalama Sıcaklık (°C)')
plt.axvline(x=today.timetuple().tm_yday, color='green', linestyle='--', label='Bugün')
plt.legend()
plt.show()
