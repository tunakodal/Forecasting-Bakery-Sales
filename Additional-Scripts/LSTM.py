import numpy as np
import pandas as pd
from meteostat import Point, Daily
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt
from datetime import datetime

# Konum belirleme (örnek: İstanbul, Türkiye)
location = Point(41.0082, 28.9784)

# Tarih aralığı
start = datetime(2014, 1, 1)
end = datetime(2024, 10, 13)

# Veriyi çekme
data = Daily(location, start, end).fetch()

# Verileri hazırlama
data.reset_index(inplace=True)
data['tavg'] = data['tavg'].fillna(method='ffill')  # NaN değerleri doldurma

# Sadece sıcaklık verisini al
temperature_data = data[['time', 'tavg']]

# Veriyi ölçeklendirme
scaler = MinMaxScaler(feature_range=(0, 1))
temperature_data['tavg'] = scaler.fit_transform(temperature_data[['tavg']])

# Zaman serisini oluşturma
def create_dataset(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        X.append(a)
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

# Eğitim ve test verilerini ayırma
time_step = 10
X, y = create_dataset(temperature_data['tavg'].values.reshape(-1, 1), time_step)

# Verileri LSTM formatına dönüştürme
X = X.reshape(X.shape[0], X.shape[1], 1)

# Modeli oluşturma
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Modeli eğitme
model.fit(X, y, epochs=10, batch_size=32)  # Epoch sayısını 10 olarak ayarladık

# Tahmin için son veriyi kullanma
last_data = temperature_data['tavg'].values[-time_step:].reshape(1, time_step, 1)

# Önümüzdeki 7 gün için tahmin yapma
predictions = []
for _ in range(7):
    pred = model.predict(last_data)
    predictions.append(pred[0][0])
    # Son tahmini yeni verilerle güncelle
    last_data = np.append(last_data[:, 1:, :], pred.reshape(1, 1, 1), axis=1)

# Tahmin sonuçlarını ölçekten geri döndürme
predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Tahminleri ekrana bastırma
for i, pred in enumerate(predictions, start=1):
    print(f'2024-10-{14 + i}: Tahmin Edilen Ortalama Sıcaklık: {pred[0]:.2f}°C')

# İsterseniz burada grafik de çizebilirsiniz.
plt.plot(predictions, marker='o')
plt.title('Gelecek 7 Gün İçin Tahmin Edilen Sıcaklıklar')
plt.xlabel('Gün')
plt.ylabel('Sıcaklık (°C)')
plt.xticks(ticks=range(7), labels=[f'Gün {i+1}' for i in range(7)])
plt.show()
