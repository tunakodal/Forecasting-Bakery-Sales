import numpy as np
import pandas as pd
from meteostat import Point, Daily
import matplotlib.pyplot as plt
import datetime
from statsmodels.tsa.arima.model import ARIMA

"""
15-16 civarında olmalıydı
2024-10-14 00:00:00: Tahmin Edilen Ortalama Sıcaklık: 18.23 °C
2024-10-15 00:00:00: Tahmin Edilen Ortalama Sıcaklık: 19.01 °C
2024-10-16 00:00:00: Tahmin Edilen Ortalama Sıcaklık: 19.47 °C
2024-10-17 00:00:00: Tahmin Edilen Ortalama Sıcaklık: 19.72 °C
2024-10-18 00:00:00: Tahmin Edilen Ortalama Sıcaklık: 19.73 °C
2024-10-19 00:00:00: Tahmin Edilen Ortalama Sıcaklık: 19.53 °C
2024-10-20 00:00:00: Tahmin Edilen Ortalama Sıcaklık: 19.38 °C
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
data.set_index('date', inplace=True)

# Sıcaklık verilerini alma
temperature_data = data['tavg']  # Ortalama sıcaklık
temperature_data = temperature_data.asfreq('D')  # Frekansı günlük olarak ayarlama

# ARIMA modelini oluşturma
model = ARIMA(temperature_data, order=(5, 1, 0))  # (p, d, q) değerlerini ayarlayabilirsin
model_fit = model.fit()

# Gelecek günler için tahmin yapma
n_days_ahead = 7
forecast = model_fit.forecast(steps=n_days_ahead)

# Sonuçları yazdırma
future_dates = [temperature_data.index[-1] + datetime.timedelta(days=i) for i in range(1, n_days_ahead + 1)]
forecast_series = pd.Series(forecast, index=future_dates)

print("Gelecek 7 Gün İçin Tahmin Edilen Ortalama Sıcaklık:")
for date, temp in forecast_series.items():
    print(f"{date}: Tahmin Edilen Ortalama Sıcaklık: {temp:.2f} °C")

# Tahminleri görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(temperature_data.index, temperature_data, label='Gerçek Veriler', color='blue')
plt.plot(forecast_series.index, forecast_series, label='Tahmin Edilen Değerler', color='red', linestyle='--')
plt.title('Sıcaklık Tahmini - ARIMA')
plt.xlabel('Tarih')
plt.ylabel('Ortalama Sıcaklık (°C)')
plt.axvline(x=temperature_data.index[-1], color='green', linestyle='--', label='Son Veri')
plt.legend()
plt.show()
