# Gerekli kütüphaneler
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Örnek veri yükleme (hava durumu verisi: sıcaklık vs.)
# data.csv içerisinde 'Date' ve 'Temperature' kolonları olduğunu varsayıyoruz
df = pd.read_csv('weather_data.csv', parse_dates=['Date'], index_col='Date')

# ARIMA modeli için sadece sıcaklık verisini alalım
temperature_data = df['Temperature']

# ARIMA modeli tanımlama (p, d, q: AR, I, MA parametreleri)
model = ARIMA(temperature_data, order=(5, 1, 0))
model_fit = model.fit()

# Tahmin yapma
forecast = model_fit.forecast(steps=30)  # 30 gün sonrası için tahmin

# Sonuçları görselleştirme
plt.plot(temperature_data, label='Actual Temperature')
plt.plot(forecast, label='Forecasted Temperature', color='red')
plt.legend()
plt.show()
