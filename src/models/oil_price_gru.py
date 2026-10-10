#GRU Model For Forecasting Oil Price
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data/normalized/oil_price_normalized.csv')

feature_columns = df[['Year', 'Month', 'Day']]
label_columns = df[['Average Price', 'Brent Price', 'WTI Price']]

features = feature_columns.values
labels = label_columns.values

timesteps = 10

sequences = []
labels_list = []

for i in range(len(features) - timesteps):
    sequences.append(features[i:i+timesteps])
    labels_list.append(labels[i+timesteps])

sequences = np.array(sequences)
labels = np.array(labels_list)

feature_train, feature_temp, labels_train, labels_temp = train_test_split(sequences, labels, test_size=0.8, random_state=42)
feature_val, feature_test, labels_val, labels_test = train_test_split(feature_temp, labels_temp, test_size=0.5, random_state=42)

model = Sequential()
model.add(GRU(64, activation='relu', input_shape=(timesteps, features.shape[1]), return_sequences=True))
model.add(GRU(32, activation='relu', return_sequences=False))
model.add(Dense(3))

#Metrics
def root_mean_squared_error(y_true, y_pred):
    return tf.sqrt(tf.reduce_mean(tf.square(y_pred - y_true)))

def r2_score(y_true, y_pred):
    ss_res = tf.reduce_sum(tf.square(y_true - y_pred))
    ss_tot = tf.reduce_sum(tf.square(y_true - tf.reduce_mean(y_true)))
    return 1 - (ss_res / ss_tot)

def mean_absolute_percentage_error(y_true, y_pred):
    return tf.reduce_mean(tf.abs((y_true - y_pred) / y_true)) * 100

model.compile(optimizer='adam',
              loss='mse',
              metrics=[root_mean_squared_error, r2_score, mean_absolute_percentage_error])

model.fit(feature_train, labels_train, epochs=50, batch_size = 32, validation_data=(feature_val, labels_val))

test_loss , test_rmse, test_r2, test_mape = model.evaluate(feature_test, labels_test)
print(f'Test Loss: {test_loss}, Test MAPE: {test_mape}, Test RMSE: {test_rmse}, Test R2: {test_r2}')