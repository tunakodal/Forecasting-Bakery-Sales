#LSTM Model For Forecasting Weather Data
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('combined_weather_dataset_normalized.csv')

feature_columns = df[['Year', 'Month', 'Day']]
label_columns = df[['tmax', 'tmin', 'tavg', 'wspd', 'pres']]
label_columns['pres'] = label_columns['pres'] / 1000 # milibar to bar

features = feature_columns.values
labels = label_columns.values

timesteps = 10

def create_sequences(features, labels, timesteps):
  sequences = []
  labels_list = []
  for i in range(len(features) - timesteps):
    seq = features[i:i+timesteps]
    label = labels[i+timesteps]
    sequences.append(seq)
    labels_list.append(label)
  return np.array(sequences), np.array(labels_list)

sequences, labels = create_sequences(features, labels, timesteps)

feature_train, feature_temp, labels_train, labels_temp = train_test_split(sequences, labels, test_size=0.8, random_state=42)
feature_val, feature_test, labels_val, labels_test = train_test_split(feature_temp, labels_temp, test_size=0.5, random_state=42)

model = Sequential()
model.add(LSTM(64, activation='relu', input_shape=(timesteps, features.shape[1]), return_sequences=True))
model.add(LSTM(32, activation='relu', return_sequences=False))
model.add(Dense(5))

#Metrics
def root_mean_squared_error(y_true, y_pred):
    return tf.sqrt(tf.reduce_mean(tf.square(y_pred - y_true)))

def r2_score(y_true, y_pred):
    ss_res = tf.reduce_sum(tf.square(y_true - y_pred))
    ss_tot = tf.reduce_sum(tf.square(y_true - tf.reduce_mean(y_true)))
    return 1 - (ss_res / ss_tot)

huber_loss = tf.keras.losses.Huber(delta=1.0)

model.compile(optimizer='adam',
              loss=huber_loss,
              metrics=[root_mean_squared_error, r2_score])

model.fit(feature_train, labels_train, epochs=500, batch_size = 32, validation_data=(feature_val, labels_val))

test_loss , test_rmse, test_r2 = model.evaluate(feature_test, labels_test)
print(f'Test Huber Loss: {test_loss}, Test RMSE: {test_rmse}, Test R2: {test_r2}')