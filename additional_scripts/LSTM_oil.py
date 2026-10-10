import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

# Petrol fiyatı verisini çekme (örneğin WTI petrolü için 'CL=F')
data = yf.download('CL=F', start='2010-01-01', end='2023-10-01')

# Kapanış fiyatı ile çalışalım
data = data[['Close']]

# Veriyi ölçeklendirme (LSTM için)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Eğitim ve test verisini ayırma
train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size:]


# LSTM modeline uygun şekilde veri hazırlığı
def create_dataset(dataset, time_step=60):
    X, y = [], []
    for i in range(len(dataset) - time_step - 1):
        X.append(dataset[i:(i + time_step), 0])
        y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(y)


time_step = 60
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# Veriyi LSTM girişine uygun hale getirme (3D array)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# LSTM modeli oluşturma
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Modeli derleme
model.compile(optimizer='adam', loss='mean_squared_error')

# Modeli eğitme
model.fit(X_train, y_train, batch_size=16, epochs=2)

# Test verisinden geleceği tahmin etmek için son 60 günün verisini alalım
last_60_days = scaled_data[-time_step:]
last_60_days_scaled = last_60_days.reshape(1, time_step, 1)

# Önümüzdeki 30 gün için tahmin yapma
predictions = []
for i in range(30):  # 30 gün için tahmin yapıyoruz
    pred = model.predict(last_60_days_scaled)
    predictions.append(pred[0, 0])

    # Tahmin edilen değeri kullanarak veri setini güncelle
    pred_reshaped = np.array(pred).reshape(1, 1, 1)  # Tahmin edilen değeri 3D yapıya çeviriyoruz
    last_60_days_scaled = np.append(last_60_days_scaled[:, 1:, :], pred_reshaped, axis=1)

# Tahminleri orijinal ölçeğe geri döndürme
predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Tahminleri ekrana bastırma
for i in range(30):
    print(f"Tahmin edilen petrol fiyatı - Gün {i + 1}: {predictions[i][0]:.2f} USD")

# Grafik gösterimi (isteğe bağlı)
plt.figure(figsize=(16, 8))
plt.plot(np.arange(1, 31), predictions, label='Tahmin edilen fiyatlar')
plt.title('Önümüzdeki 30 Gün İçin Petrol Fiyatı Tahmini')
plt.xlabel('Gün')
plt.ylabel('Fiyat (USD)')
plt.legend()
plt.show()
