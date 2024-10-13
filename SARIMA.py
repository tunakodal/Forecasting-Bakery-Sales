# Gerekli kütüphaneler
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# Örnek veri yükleme (petrol fiyatları verisi)
# data.csv içerisinde 'Date' ve 'Oil_Price' kolonları olduğunu varsayıyoruz
df = pd.read_csv('oil_price_data.csv', parse_dates=['Date'], index_col='Date')

# SARIMA modeli için petrol fiyatları verisini alalım
oil_price_data = df['Oil_Price']

# SARIMA modeli tanımlama (p, d, q, P, D, Q, m: ARIMA ve sezonsallık parametreleri)
model = SARIMAX(oil_price_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
model_fit = model.fit()

# Tahmin yapma
forecast = model_fit.forecast(steps=12)  # 12 ay sonrası için tahmin

# Sonuçları görselleştirme
plt.plot(oil_price_data, label='Actual Oil Price')
plt.plot(forecast, label='Forecasted Oil Price', color='red')
plt.legend()
plt.show()
